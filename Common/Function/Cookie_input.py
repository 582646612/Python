#coding=utf-8
from  selenium import webdriver
import time
def input_cookie(driver):
    driver.add_cookie({'name':'BAIDUID','value':'4BC1DBE9B6556E4AC2993493AB25F985:FG=1'})
    driver.add_cookie({'name':'BDUSS', 'value':'GNMeHIyZll1S2w1aDg5elR1OUZFQ0NJanZtfk0xSWNiNno3TUdzSmdNbWRyQ05hTVFBQUFBJCQAAAAAAAAAAAEAAADf0681Y3NjODI1MDk2MDk1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJ0f~FmdH~xZW'})
    driver.refresh()
