## 旧版Pi-Star更新到WPSD定制版
### 
1.将Pi-Star程序的更新服务器改为国内的gitee + 强行覆盖 脚本sbin，dashboard, bin, sbin三个项目，适用于：官方Pi-Star(UK), WPSD(US)。执行完成后，就可以刷新仪表盘的【配置页】，进行正常的【更新主程序】【更新Id库】操作了，Id更新也变快了！
### 以下为分解执行，仅供学习研究用，无需手工执行，请忽略：
###
2.将Pi-Star程序的更新服务器改为国内的gitee代码库
###
3.强行覆盖：本地修改过的仪表盘网页文件、MMDVMHost、脚本，dashboard, bin, sbin三个项目，不包括配置文件和数据
###
4.更新系统：调用目标主机，执行系统更新命令：sudo pistar-update（不更新debian系统组件）
###
5，更新DMRID+服务器列表（国内更新快）
###
6.更新NextionDriver（屏幕）DMRID通讯录（国内更新快）
###
7.更新服务器列表（国内更新快）
###
8.卸载NextionDriver（屏幕）驱动 
###
9.安装NextionDriver（屏幕）驱动 
###
10.提升BPiM2 betty WiFi驱动稳定性问题
###
 
####
此代码抄录自BI7JTA大佬公众号《MMDVM中文帮助》[MMDVM增强工具一文](https://mp.weixin.qq.com/s/UeFkMJGIy1k0igB3dmuM_Q)