import wx
import socket
from time import sleep
import _thread as thread

HOST='localhost'
PORT=5050

class Connected:
         def __init__(self,host,port):
                  self.address=(host,port)
                 
         def C_socket(self):
                  sock=socket.socket()
                  sock.connect(self.address)
                  return sock
class LoginFrame(wx.Frame):
         def __init__(self, parent, id, title, size):
                  # 初始化，添加控件并绑定事件
                  wx.Frame.__init__(self, parent, id, title)
                  self.SetSize(size)
                  self.Center()
                  self.serverAddressLabel = wx.StaticText(self, label="Server Address", pos=(10, 50), size=(120, 25))
                  self.userNameLabel = wx.StaticText(self, label="UserName", pos=(40, 100), size=(120, 25))
                  self.serverAddress = wx.TextCtrl(self, pos=(120, 47), size=(150, 25))
                  self.userName = wx.TextCtrl(self, pos=(120, 97), size=(150, 25))
                  self.loginButton = wx.Button(self, label='Login', pos=(80, 145), size=(130, 30))
                  # 绑定登录方法
                  self.loginButton.Bind(wx.EVT_BUTTON, self.login)
                  self.Show()

         def login(self, event):
                 # 登录处理
                  try:
                           serverAddress = self.serverAddress.GetLineText(0).split(':')
                           response = con.recv(2048)
                           
                           if not b'Connect Success' in  response :
                                    self.showDialog('Error', 'Connect Fail!', (200, 100))
                                    print('error:',response.decode('utf-8'))
                                    return
                           con.send(('login ' + str(self.userName.GetLineText(0)) + '\n').encode("utf-8"))
                           response = con.recv(2048)
                           if response == b'UserName Empty':
                                    self.showDialog('Error', 'UserName Empty!', (200, 100))
                           elif response == b'UserName Exist':
                                    self.showDialog('Error', 'UserName Exist!', (200, 100))
                           else:
                                    self.Close()
                                    ChatFrame(None, 2, title='ShiYanLou Chat Client', size=(500, 400))
                  except Exception:
                           self.showDialog('Error', 'Connect Fail!', (95, 20))

         def showDialog(self, title, content, size):
                 # 显示错误信息对话框
                 dialog = wx.Dialog(self, title=title, size=size)
                 dialog.Center()
                 wx.StaticText(dialog, label=content)
                 dialog.ShowModal()

class ChatFrame(wx.Frame):
    
         def __init__(self, parent, id, title, size):
                 # 初始化，添加控件并绑定事件
                 wx.Frame.__init__(self, parent, id, title)
                 self.SetSize(size)
                 self.Center()
                 self.chatFrame = wx.TextCtrl(self, pos=(5, 5), size=(490, 310), style=wx.TE_MULTILINE | wx.TE_READONLY)
                 self.message = wx.TextCtrl(self, pos=(5, 320), size=(300, 25))
                 self.sendButton = wx.Button(self, label="Send", pos=(310, 320), size=(58, 25))
                 self.usersButton = wx.Button(self, label="Users", pos=(373, 320), size=(58, 25))
                 self.closeButton = wx.Button(self, label="Close", pos=(436, 320), size=(58, 25))
                 # 发送按钮绑定发送消息方法
                 self.sendButton.Bind(wx.EVT_BUTTON, self.send)
                 # Users按钮绑定获取在线用户数量方法
                 self.usersButton.Bind(wx.EVT_BUTTON, self.lookUsers)
                 # 关闭按钮绑定关闭方法
                 self.closeButton.Bind(wx.EVT_BUTTON, self.close)
                 thread.start_new_thread(self.receive, ())
                 self.Show()

         def send(self, event):
                 # 发送消息
                  message = str(self.message.GetLineText(0)).strip()
                  if message != '':
                           con.sendall(('say ' + message + '\n').encode("utf-8"))
                           self.message.Clear()
         def lookUsers(self, event):
                 # 查看当前在线用户
                  con.send(b'look\n')

         def close(self, event):
                 # 关闭窗口
                 con.send(b'logout\n')
                 con.close()
                 self.Close()

         def receive(self): 
                  # 接受服务器的消息
                  while True:
                           sleep(0.6)
                           result = con.recv(4096)
                  if result != '':
                           self.chatFrame.AppendText(result)

if __name__ == '__main__':
         app = wx.App()
         con=Connected(HOST,PORT).C_socket()
         print(con)
         LoginFrame(None, -1, title="Login", size=(320, 250))
         app.MainLoop()


