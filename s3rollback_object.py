import boto3
import logging
from operator import attrgetter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

def rollback_object(bucket, object_key, version_id):
    """
    Rolls back an object to an earlier version by deleting all versions that
    occurred after the specified rollback version.

    Usage is shown in the usage_demo_single_object function at the end of this module.

    :param bucket: The bucket that holds the object to roll back.
    :param object_key: The object to roll back.
    :param version_id: The version ID to roll back to.
    """
    # Versions must be sorted by last_modified date because delete markers are
    # at the end of the list even when they are interspersed in time. (This is because
    # when we use the builtin sorted method, it ensures this to be true. [if we sort ascending, then
    # the delete markers would always be on top])
    versions = sorted(
        bucket.object_versions.filter(Prefix=object_key), #note "prefix" means will delete "questions copy" if newer than version we are rolling back to.
        key=attrgetter("last_modified"), #note this code will also delete the delete marker if it is newer than the version we are rolling back to.
        reverse=True,
    )
    
    if object_key[-1]=='/':
        filtered_versions = versions
    else:
        filtered_versions = [v for v in versions if v.key == object_key]

    logger.debug(
        "Got versions:\n%s",
        "\n".join(
            [
                f"\t{version.version_id}, last modified {version.last_modified}, name {version.key}"
                for version in filtered_versions
            ]
        ),
    )

    if version_id in [ver.version_id for ver in filtered_versions]:
        print(f"Rolling back to version {version_id}")
        for version in filtered_versions:
            if version.version_id != version_id:
                version.delete()
                print(f"Deleted version {version.version_id}")
            else:
                break #we break so as not to delete versions BEFORE the one we are rolling back to

        print(f"Active version is now {bucket.Object(object_key).version_id} for object {bucket.Object(object_key).key}")
            #note this assume object_key is the FULL key not a prefix
    else:
        raise KeyError(
            f"{version_id} was not found in the list of versions for " f"{object_key}."
        )


if __name__ == '__main__':
   mybucket = boto3.resource('s3').Bucket('scottedwards2000') 
   result = rollback_object(mybucket, 'questions', 'RQY0ebFXtUnm.A48N2I62CEmdu2QZGEO')
   print(result)
