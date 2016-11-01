# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:27:51 2016

@author: codeWorm
"""

import gym 

env = gym.make('CartPole-v0')
env.reset()
for _ in range (1000):
    env.render()
    env.step(env.action_space.sample())
    
