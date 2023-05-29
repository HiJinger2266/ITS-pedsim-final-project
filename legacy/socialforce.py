import numpy as np
import pandas as pd
import agent as ag

# socialforce.py 運作方式類似 math 或 numpy，以 method 為主要呼叫方式，而非 class
global coefA_r_bound, coefB_r_bound, coefA_a_bound, coefB_a_bound
global coefA_inact_ped_stre, coefB_inact_ped_dist, coefB_inact_ped_time
global coefA_inact_veh, coefB_inact_veh, coefA_signal, coefB_signal

# Reference: "A Modified Social Force Model for Pedestrian Behavior Simulation at Signalized Crosswalks"
# In the thesis, alpha means itself, beta means other agents
coefA_r_bound = 0.23
coefB_r_bound = 0.65
coefA_a_bound = 0.51
coefB_a_bound = 0.93
coefA_inact_ped_stre = 0.81
coefB_inact_ped_dist = 0.74
coefB_inact_ped_time = 0.34
coefA_inact_veh = 1.29
coefB_inact_veh = 0.96
coefA_signal = 0.12
coefB_signal = 0.09

# Social Force 由五向組成，必須傳遞同一個 Agent (Ped or Bike) 進去計算現況，最後加總輸出
def SocialForce(agent):
    forcedriving = ForceDriving(agent=agent)
    forceped = ForcePed(agent=agent)
    forceboundary = ForceBoundary(agent=agent)
    forcevehicle = ForceVehicle(agent=agent)
    forcesignal = ForceSignal(agent=agent)
    socialforce_x = forcedriving[0] + forceped[0] + forceboundary[0] + forcevehicle[0] + forcesignal[0]
    socialforce_y = forcedriving[1] + forceped[1] + forceboundary[1] + forcevehicle[1] + forcesignal[1]
    return [socialforce_x, socialforce_y]

# Driving force toward destination
def ForceDriving(agent):
    tau_alpha = agent.relax_time_s              # 休息時間 is Scalar
    e_alpha_vec = agent.unit_target_vec         # 單位目標向量 is Vector
    desire_speed = agent.desired_speed_mps      # 期望速度純量 is Scalar
    current_speed_vec = agent.velocity_vec      # 速度向量 is Vector
    f_x = (desire_speed * e_alpha_vec[0] - current_speed_vec[0]) / tau_alpha
    f_y = (desire_speed * e_alpha_vec[1] - current_speed_vec[1]) / tau_alpha
    return [f_x, f_y] 

# Repulsive force from surrounding pedestrians
def ForcePed(agent):
    return [0, 0]

# Repulsive or attractive force from crosswalk boundary
def ForceBoundary(agent):
    return [0, 0]
    
# Repulsive force from conflicting vehicles (Not to be developed in this project)
def ForceVehicle(agent):
    return [0, 0]

# Attractive force from signal phase
def ForceSignal(agent):
    return [0, 0]