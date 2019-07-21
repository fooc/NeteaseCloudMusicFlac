#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


orign_url='http://pan.baidu.com'# 百度云官网链接
username= 'lycatbd' # 百度云账号
userpass= 'lyc@baidu' # 百度云密码

# 更改浏览器的默认下载路径
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\Downloads'}# 默认下载目录
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(executable_path='E:\\CodeHub\\music-crawl\\chromedriver.exe', options=options)# Chromedriver.exe的系统路径


# browser=webdriver.Chrome()


browser.get(orign_url)# 打开百度云官网链接
time.sleep(5)# 等待浏览器打开页面
login_static=browser.find_element_by_id('TANGRAM__PSP_4__footerULoginBtn')# 选择账号密码登录
login_static.click()
time.sleep(3)
login_username=browser.find_element_by_id('TANGRAM__PSP_4__userName')
login_username.clear()
login_username.send_keys(username)# 输入用户名
time.sleep(2)
login_userpass=browser.find_element_by_id('TANGRAM__PSP_4__password')
login_userpass.clear()
login_userpass.send_keys(userpass)# 输入用户密码
time.sleep(2)

input('please input verify code and press login, and then press enter here')
# verify_code = input('Please enter the verify code here for login (press Enter to submit):')
# login_verifyCode=browser.find_element_by_id('TANGRAM__PSP_4__verifyCode')
# login_verifyCode.clear()
# login_verifyCode.send_keys(verify_code)
# time.sleep(2)
# login_submit=browser.find_element_by_id('TANGRAM__PSP_4__submit')
# login_submit.click()# 提交
# time.sleep(5)

# url='https://pan.baidu.com/share/init?surl=TdGJC62PctLHHg8yhF44SA'# 资源链接
# browser.get(url)
# select_all=browser.find_element_by_class_name('zbyDdwb')
# select_all.click()# 点击【全选】
# time.sleep(2)
# download=browser.find_element_by_class_name('icon-download')
# download.click()# 点击【下载】
# time.sleep(2)
# #common_download=browser.find_element_by_id('_disk_id_2')
# #common_download.click()# 点击【会员下载】，如果你是会员的话
# #time.sleep(2)
# common_download=browser.find_element_by_id('_disk_id_3')
# common_download.click()# 点击【普通下载】



#百度云分享的地址
url = "https://pan.baidu.com/share/init?surl=TdGJC62PctLHHg8yhF44SA"
#分享密码
pwd = "m9ru"
#这里要传入chromedriver.exe的地址，或者将该文件放到待执行python脚本的同目录下
browser = webdriver.Chrome("E:\\CodeHub\\music-crawl\\chromedriver.exe")
#请求连接
browser.get(url)
#这里休息一下让浏览器加载页面，否则可能因获取不到元素报错，下面的sleep同理
time.sleep(1)
#获取输入分享密码的输入框(右键审查元素，找到对应的输入框,然后可以查看到其类为QKKaIE)
input_ =  browser.find_element(By.CLASS_NAME,"QKKaIE")
#将密码自动填充到输入框
input_.send_keys(pwd, Keys.ARROW_DOWN)
#获取提交按钮
submit_button = browser.find_element(By.CLASS_NAME,"text")
#提交
submit_button.click()

time.sleep(1)
#获取下载按钮,这里下载按钮没有直接给可以区分的类名所以用xpath方式获取(其实我也不懂什么是xpath在网上找的)
download_btn = browser.find_element(By.CLASS_NAME,"x-button-box").find_element_by_xpath('//*[@data-button-id="b3"]')
#下载
download_btn.click()
#关闭资源
browser.close()
