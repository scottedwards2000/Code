import pandas as pd
import numpy as np

# record prob output drawn to decide the argmax into a dataframe

print("\n Bayesian Bandit using Thompson Sampling \n")
print("Goal is to maximize the attempts on the highest converting variant")


N = 5  #Number of Variants

trials = 2000   #how many total pulls do we want to do?

trial_data =[]  # array of trial #'s (for display at end)

machine_data=[] # array of which handles we pulled on each trial (for display at end)

win_loss=[] #array of whether we won or lost on each trial (for display at end)



means = np.array([0.9, 0.75, 0.5, 0.25, 0.1])  # Define the actual conversion rates for each machine (unknown in real life)


probs = np.zeros(N) #temp storage for single trial: random sample from posterior probability distribution for each machine(EV = the mean?)
   #NOTE: this simply determines which machine to pull(the handle of machine with the higest one of these will be pulled)

prob_df = pd.DataFrame(columns=['p0','p1','p2','p3','p4']) #holds the history of probs (above) from each trial



beta_mean = np.zeros(N) #temporary storage for a single trial: I will take the mean of a random sample from the same posterior distributions used above for probs (just to show it)

beta_mean_df = pd.DataFrame(columns=['p0','p1','p2','p3','p4']) #holds the history of beta_mean's (above) from each trial


S = np.zeros(N, dtype=int)  # running count of successes for each machine
F = np.zeros(N, dtype=int)  # running count of failures for each machine
pulls = np.zeros(N, dtype=int) # running count of pulls for each machine (just used at end for display)

rnd = np.random.RandomState()  #random series for machine payouts and Beta (put in a number to replicate series)




show_each_trial = 0#1 #change to 1 if you want to print each trial (otherwise only prints last one)

def prints(*args, **kwargs):
    if show_each_trial == 1:
        if kwargs=="":print(*args, **kwargs, end="")
        else: print(*args, **kwargs)
    elif trial >= trials-1:
        if kwargs=="":print(*args, *kwargs, end="")
        else: print(*args, **kwargs)

def samples():
  if show_each_trial == 1:
    return 30000#000
  elif trial >= trials-1:
    return 3000000
  else:
    return 3 #no need for precision if we aren't going to display the mean for this trial
 
for trial in range(trials):
    
    prints("\nTrial " + str(trial))
    
    trial_data.append(trial) #append this trial # to the trial_data array we defined above
    
    #for the new trial, clear out the probabilities we use to decide which machine to pull (see above desc for same variable)
    #probs = np.zeros(N)
    
    #pull from the posterior probability distribution for each machine to get the prob for it (again, just used to pick handle)
    for i in range(N): 
      
      probs[i] = rnd.beta(S[i] + 1, F[i] + 1) #since we are using a beta(1,1) prior, this is the posteror prob.
    
      beta_mean[i] = np.mean(rnd.beta(S[i] + 1, F[i] + 1, samples())) #last number is how many samples to pull to calc mean

      #global prob_df  #i guess this isn't needed anymore b/c I'm not modifying it inside a function
      if i == 4: #last machine
        columns = ['p0','p1','p2','p3','p4']  
        
        df = pd.DataFrame(probs, index=columns).T 
        prob_df = pd.concat([prob_df, df], ignore_index = True) #save the probs for this trial
        
        df = pd.DataFrame(beta_mean, index=columns).T
        beta_mean_df = pd.concat([beta_mean_df, df], ignore_index = True) #save the means of the dist's used to get the probs
        
      else:
        pass
  
    prints("means of posterior probability dist (this should get closer to actual over time)")
    for i in range(N):
        prints('%0.4f ' % beta_mean[i], end='')
        
    prints("")
    
    prints("sampling probs =  ")
    for i in range(N):
      prints("%0.4f  " % probs[i], end="")

      
    prints("")

    machine = np.argmax(probs)
    prints("Playing machine " + str(machine))
    
    machine_data.append(machine)
    # Updates success and fails in real life we can can update conversions , clicks, or whatever success of chosen variant
    
    p = rnd.random_sample()  # [0.0, 1.0)
    prints(p)
    if p < means[machine]:
          prints(" -- win")
          S[machine] += 1
          win_loss.append('W')
    else:
          prints(" -- lose")
          F[machine] += 1
          win_loss.append('L')

    prints("\nSuccess vector: ", end="")
    prints(S)
    prints("Failure vector: ", end="")
    prints(F)
    prints("Total pulls: ", end="")
    pulls=[S[i]+F[i] for i in range(len(S))]
    prints(pulls)
    
