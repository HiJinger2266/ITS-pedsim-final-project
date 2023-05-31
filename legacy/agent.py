import numpy as np
import pandas as pd
import socialforce as scf

global timestep_s
timestep_s = 1    # 全域使用時間間隔 1 秒

# Matplotlib 直接點點點

# X 向右為正，Y 向上為正
class Agent(object):
    def __init__(self, startpoint, endpoint):
        print("Agent created")

        # Parameters from thesis
        self._visual_range_deg = 170
        self._visual_radius_m = 8
        self._desired_speed_mps = np.random.normal(1.6, 0.15)
        self._relax_time_s = np.random.normal(2.2, 0.5)
        self._max_accept_speed_mps = np.random.normal(1.8, 0.3)
        self._speed_change_mps = np.random.normal(-0.07, 0.09)
        self._direction_change_deg = np.random.normal(0.03, 2.14)

        # Initialize
        self._arrived = False           # 自行車或行人是否抵達目的地，if True, delete itself instance
        self._in_boundary = True        # 是否位於行穿線內
        self._neighbors = []            # 周遭物件，動態陣列，通常只留有影響力的
        self._moveable = True           # 綠燈時允許通行，紅燈時必須往最近的分隔島休息

        # Finalize
        self._end_x_m = endpoint[0]     # 目標位置 X 座標 (m)
        self._end_y_m = endpoint[1]     # 目標位置 Y 座標 (m)
        
        # Status
        self._pos_x_m = startpoint[0]                           # 初始位置 X 座標 (m)
        self._pos_y_m = startpoint[1]                           # 初始位置 Y 座標 (m)
        self._speed_mps = np.random.normal(1, 0.5)              # 初始速率 (m/s)
        self._direction_x = self.unit_target_vec[0]           # 初始方向 X 比例
        self._direction_y = self.unit_target_vec[1]           # 初始方向 Y 比例
        self._vel_x_mps = self._speed_mps * self._direction_x   # 初始速度 X 方向 (m/s)
        self._vel_y_mps = self._speed_mps * self._direction_y   # 初始速度 Y 方向 (m/s)
        self._acc_x_mpss = scf.SocialForce(self)[0]             # 初始加速度 X 方向 (m/s^2)
        self._acc_y_mpss = scf.SocialForce(self)[1]             # 初始加速度 Y 方向 (m/s^2)
        
    def update(self):
        self._acc_x_mpss = scf.SocialForce(self)[0]         # 加速度 X 方向 (m/s^2)
        self._acc_y_mpss = scf.SocialForce(self)[1]         # 加速度 Y 方向 (m/s^2)
        self._vel_x_mps = self._vel_x_mps + self._acc_x_mpss * timestep_s     # 速度 X 方向 (m/s)
        self._vel_y_mps = self._vel_y_mps + self._acc_y_mpss * timestep_s     # 速度 Y 方向 (m/s)
        self._pos_x_m = self._pos_x_m + self._vel_x_mps * timestep_s        # 位置 X 座標 (m)
        self._pos_y_m = self._pos_y_m + self._vel_y_mps * timestep_s        # 位置 Y 座標 (m)
        self_arrived = self.check_arrival()
    
    def check_surround_ped(self):
        pass

    @property   # 當前位置向量 (m, m)
    def position_vec(self):
        return [self._pos_x_m, self._pos_y_m]
    
    @property   # 當前速度向量 (m/s, m/s)
    def velocity_vec(self):
        return [self._vel_x_mps, self._vel_y_mps]
    
    @property   # 當前加速度向量 (m/s^2, m/s^2)
    def acceleration_vec(self):
        return [self._acc_x_mpss, self._acc_y_mpss]
    
    @property   # 當前速度純量 (m/s)
    def velocity_sca(self):
        return np.sqrt(np.square(self._vel_x_mps) + np.square(self._vel_y_mps))
    
    @property   # 當前加速度純量 (m/s^2)
    def acceleration_sca(self):
        return np.sqrt(np.square(self._acc_x_mpss) + np.square(self._acc_y_mpss))
    
    @property   # 目標向量 (m, m)
    def target_vec(self):
        target_x = self._end_x_m - self._pos_x_m
        target_y = self._end_y_m - self._pos_y_m
        return [target_x, target_y]
    
    @property   # 剩餘距離 (m)
    def remain_distance_m(self):
        target_x = self.target_vec[0]
        target_y = self.target_vec[1]
        return np.sqrt(np.square(target_x) + np.square(target_y))
    
    @property   # 單位目標向量
    def unit_target_vec(self):
        try:
            unit_target_x = self.target_vec[0] / self.remain_distance_m
            unit_target_y = self.target_vec[1] / self.remain_distance_m
            return [unit_target_x, unit_target_y]
        except:
            return [0, 0]
        
    @property   # 視野 (Two Vectors)
    def visual_range(self):
        pass

    @property
    def relax_time_s(self):
        return self._relax_time_s

    @property
    def desired_speed_mps(self):
        return self._desired_speed_mps
    
    # 檢查是否快到終點，若差不多，就可以結束任務
    def check_arrival(self):
        if self.remain_distance_m <= 1:
            print("Agent mission completed")
            return True
        else:
            return False
    
    def destroy(self):
        del self
            
class Pedestrian(Agent):
    def __init__(self, startpoint, endpoint):
        super(self).__init__(startpoint, endpoint)



if __name__ == "__main__":
    wow = Agent(startpoint=[18,30],endpoint=[425,66])
    print(wow.target_vec)
    i=1
    while wow.check_arrival() == False:
        wow.update()
        print("Step " + str(i))
        #print(wow.position_vec)
        #print(wow.velocity_vec)
        #print(wow.acceleration_vec)
        print("Remain distance meter:", wow.remain_distance_m)
        i=i+1
    
    
    
#Bike, Ped



# 利用 python 理解 mvc 架構模型
# https://www.twblogs.net/a/5be9b2b22b717720b51e5405