#coding:utf-8
import psutil
#pip install psutil
print(psutil.cpu_count())# CPU逻辑数量
print(psutil.cpu_count(logical=False))# CPU物理核心
print(psutil.cpu_times())
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))
print(psutil.virtual_memory())#物理内存
print(psutil.swap_memory())#交换内存
psutil.disk_partitions() # 磁盘分区信息
psutil.disk_usage('/') # 磁盘使用情况
psutil.disk_io_counters() # 磁盘IO
psutil.net_io_counters() # 获取网络读写字节／包的个数
psutil.net_if_addrs() # 获取网络接口信息
psutil.net_if_stats() # 获取网络接口状态
psutil.net_connections()

print(psutil.pids()) # 所有进程ID
p = psutil.Process(6092) # 获取指定进程ID=3776，其实就是当前Python交互环境
p.name() # 进程名称
p.exe() # 进程exe路径
p.cwd() # 进程工作目录
p.cmdline() # 进程启动的命令行
p.ppid() # 父进程ID
p.parent() # 父进程
p.children() # 子进程列表
p.status() # 进程状态
p.username() # 进程用户名
p.create_time() # 进程创建时间
p.terminal() # 进程终端
p.cpu_times() # 进程使用的CPU时间
p.memory_info() # 进程使用的内存
p.open_files() # 进程打开的文件
p.connections() # 进程相关网络连接
p.num_threads() # 进程的线程数量
p.threads() # 所有线程信息
p.environ() # 进程环境变量
p.terminate() # 结束进程