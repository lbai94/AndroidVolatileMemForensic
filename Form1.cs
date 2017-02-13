using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using System.Threading;

namespace getmem_gui
{
    public partial class Form1 : Form
    {
        string SaveFileName;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string exepath = AppDomain.CurrentDomain.BaseDirectory;
            string path = exepath + "meminfo.bat";
            Process p = new Process();

            //Process类有一个StartInfo属性，这个是ProcessStartInfo类，包括了一些属性和方法，下面我们用到了他的几个属性：设定程序名
            p.StartInfo.FileName = path;
            //p.StartInfo.FileName = "D:\\thesis\\getmem\\command.bat";
            //关闭Shell的使用

            p.StartInfo.UseShellExecute = false;

            //重定向标准输入

            p.StartInfo.RedirectStandardInput = true;

            //重定向标准输出

            p.StartInfo.RedirectStandardOutput = true;

            //重定向错误输出

            p.StartInfo.RedirectStandardError = true;

            //设置不显示窗口

            p.StartInfo.CreateNoWindow = true;

            //上面几个属性的设置是比较关键的一步。既然都设置好了那就启动进程吧，

            p.Start();
            //Thread.Sleep(6000);
            //Application.DoEvents();
            
            //  输入要执行的命令
           // p.StandardInput.WriteLine("adb shell su -c 'dumpsys meminfo'");
            //p.StandardInput.WriteLine("adb pull sdcard/meminfo/8769.mem D:\thesis");
           // p.StandardInput.WriteLine("exit");

            //从输出流获取命令执行结果，

            string strRst = "";
            string line = "";
           // bool start = false;
            string process_class="";
            int process_num = 0;
            string processes = "";
            int index=0;
           /* while ((line = p.StandardOutput.ReadLine()) != null)
            {
                if (line.Contains("USER")) 
                {
                    strRst += line;
                    strRst += "\r\n";
                    start = true;
                }
                else if (line.Contains("exit"))
                    break;
                else if (start)
                {
                    strRst += line;
                    strRst += "\r\n";
                }
                    
            }*/
            /*strRst = p.StandardOutput.ReadToEnd();
            FileStream fs = new FileStream("meminfo.txt",FileMode.Create);
            StreamWriter sw = new StreamWriter(fs, Encoding.Default);
            sw.Write(strRst);
            sw.Close();
            fs.Close();
            FileStream File = new FileStream(SaveFileName, FileMode.Open);
            StreamReader sr = new StreamReader(File, Encoding.Default, true);*/

            while ((line=p.StandardOutput.ReadLine() )!= null)
            {
                if (line.Contains(": Native"))
                {
                    process_class = "Native";
                    process_num = 0;
                    processes = "";
                }
                else if(line.Contains(": System"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "System";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": Persistent"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "Persistent";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": Foreground"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "Foreground";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": Visible"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "Visible";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": Perceptible"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "Perceptible";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": A Services"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "A Services";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": Home"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "Home";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": Previous"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "Previous";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": B Services"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "B Services";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains(": Cached"))
                {
                    strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
                    strRst += processes;
                    process_class = "Cached";
                    process_num = 0;
                    processes = "";
                }
                else if (line.Contains("(pid")){
                    index = line.IndexOf(":");
                    processes += line.Substring(index + 1);
                    processes += "\r\n";
                    process_num++;
                }
                else if (line.Contains("Total PSS by category:"))
                {
                    break;
                }

            }
            strRst = strRst + "进程类别：" + process_class + " 进程数量：" + process_num + "\r\n";
            strRst += processes;
           
            p.Close();
            meminfo.Text = strRst;
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void getmem_Click(object sender, EventArgs e)
        {
            string exepath = AppDomain.CurrentDomain.BaseDirectory;
            string path = exepath + "command.bat";
            FileInfo fi1 = new FileInfo(path);
            string id = inputPID.Text;

            if (fi1.Exists)
                fi1.Delete();

            //Create a file to write to.
            using (StreamWriter sw = fi1.CreateText())
            {
                sw.WriteLine("adb shell su -c 'chmod 777 /data'");
                sw.WriteLine("adb shell su -c './data/mem_heap " + id + " sdcard/" + id + ".mem'");
                sw.WriteLine("adb pull sdcard/" + id + ".mem " + Application.StartupPath);
                sw.WriteLine("adb shell su -c 'rm sdcard/" + id + ".mem'");
                sw.WriteLine("exit");
            }

            Process p = new Process();

            //Process类有一个StartInfo属性，这个是ProcessStartInfo类，包括了一些属性和方法，下面我们用到了他的几个属性：设定程序名
            // p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.FileName = path;
            //关闭Shell的使用

            p.StartInfo.UseShellExecute = false;

            //重定向标准输入

            p.StartInfo.RedirectStandardInput = true;

            //重定向标准输出

            p.StartInfo.RedirectStandardOutput = true;

            //重定向错误输出

            p.StartInfo.RedirectStandardError = true;

            //设置不显示窗口

            p.StartInfo.CreateNoWindow = true;

            //上面几个属性的设置是比较关键的一步。既然都设置好了那就启动进程吧，

            p.Start();

            //从输出流获取命令执行结果，

            string strRst = p.StandardOutput.ReadToEnd();
            p.Close();
        }

           private void meminfo_TextChanged(object sender, EventArgs e)
           {
           
           }

           private void phone_state_TextChanged(object sender, EventArgs e)
           {
           
           }

           private void button_phone_Click(object sender, EventArgs e)
           {
             string exepath = AppDomain.CurrentDomain.BaseDirectory;
             string path = exepath + "get_config.bat";
             Process p = new Process();

            //Process类有一个StartInfo属性，这个是ProcessStartInfo类，包括了一些属性和方法，下面我们用到了他的几个属性：设定程序名
             p.StartInfo.FileName = path;
            //p.StartInfo.FileName = "D:\\thesis\\getmem\\command.bat";
            //关闭Shell的使用

            p.StartInfo.UseShellExecute = false;

            //重定向标准输入

            p.StartInfo.RedirectStandardInput = true;

            //重定向标准输出

            p.StartInfo.RedirectStandardOutput = true;

            //重定向错误输出

            p.StartInfo.RedirectStandardError = true;

            //设置不显示窗口

            p.StartInfo.CreateNoWindow = true;

            //上面几个属性的设置是比较关键的一步。既然都设置好了那就启动进程吧，

            p.Start();
            Thread.Sleep(1000);
            Application.DoEvents();
            //  输入要执行的命令


            //从输出流获取命令执行结果，

           // string strRst = p.StandardOutput.ReadToEnd();
            string strRst="";
            string line="";
            while((line=p.StandardOutput.ReadLine())!=null){
                if(line.Contains("ro.product.device")){
                    while((line=p.StandardOutput.ReadLine())!=null){
                        if(!line.StartsWith("*")) {
                            //strRst=line;
                            break;
                        }
                    }
                    if(line==""){
                        strRst="无法检测到你的手机！请检查连接！";
                        break;
                    }
                    else{
                        strRst+="手机型号： "+line+" ";
                    }
                }
                else if(line.Contains("ro.product.manufacturer")){
                    strRst+="制造商： "+p.StandardOutput.ReadLine()+"\r\n";
                }
                else if(line.Contains("ril.cdma.deviceid")){
                    strRst+="序列号： "+p.StandardOutput.ReadLine()+"   ";
                }
                else if(line.Contains("ro.build.version.release")){
                    strRst+="系统版本： "+p.StandardOutput.ReadLine()+"\r\n";
                }
                else if(line.Contains("dalvik.vm.heapsize")){
                    strRst+="Dalvik VM可使用堆内存： " +p.StandardOutput.ReadLine() +"\r\n";
                }
                else if (line.Contains("su -c"))
                {
                    strRst += "Root权限： ";
                    line = p.StandardOutput.ReadLine();
                    if (line.Contains("option requires"))
                    {
                        strRst += "已获取";
                    }
                    else
                    {
                        strRst += "未获取，您无法使用本软件其他功能";
                    }
                }
            }
            p.Close();
            phone_state.Text = strRst;
           }

           private void button_analysis_Click(object sender, EventArgs e)
           {
               OpenFileDialog openFileDialog = new OpenFileDialog();
               openFileDialog.InitialDirectory = AppDomain.CurrentDomain.BaseDirectory;
               if (openFileDialog.ShowDialog(this) == DialogResult.OK)
               {
                   string FileName = openFileDialog.FileName;
                   Process p = new Process();

                 //  FileInfo fi1 = new FileInfo(path);
                   //string id = inputPID.Text;

                   //Process类有一个StartInfo属性，这个是ProcessStartInfo类，包括了一些属性和方法，下面我们用到了他的几个属性：设定程序名
                   //p.StartInfo.FileName = path;
                     p.StartInfo.FileName = "cmd.exe";
                   //p.StartInfo.FileName = @"%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe";
                   //p.StartInfo.FileName = "D:\\thesis\\getmem\\command.bat";
                   //关闭Shell的使用

                   p.StartInfo.UseShellExecute = false;

                   //重定向标准输入

                   p.StartInfo.RedirectStandardInput = true;

                   //重定向标准输出

                   p.StartInfo.RedirectStandardOutput = true;

                   //重定向错误输出

                   p.StartInfo.RedirectStandardError = true;

                   //设置不显示窗口

                   p.StartInfo.CreateNoWindow = true;

                   //上面几个属性的设置是比较关键的一步。既然都设置好了那就启动进程吧，

                   p.Start();

                   //  输入要执行的命令
                   if (comboBox1.SelectedItem.ToString()== "网易邮箱")
                   {
                       //SaveFileName = "163_result.txt";
                       p.StandardInput.WriteLine("python Analysis_163.py " + FileName + " " + SaveFileName);
   
                   }
                   else if(comboBox1.SelectedItem.ToString()== "陌陌"){
                       //SaveFileName = "momo_result.txt";
                       p.StandardInput.WriteLine("python Analysis_momo.py " + FileName + " " + SaveFileName);
                   
                   }
                   else if (comboBox1.SelectedItem.ToString() == "微信(支付)")
                   {
                       //SaveFileName = "wechat_result.txt";
                       p.StandardInput.WriteLine("python Analysis_wcpay.py " + FileName + " " + SaveFileName);
                   
                   }
                   p.StandardInput.WriteLine("exit");
                   //从输出流获取命令执行结果，
                  // string strRst = p.StandardOutput.ReadToEnd();
                   p.Close();
                   //Thread.Sleep(4000);
                   //Application.DoEvents();
                   
                   result.Text = "分析完成，分析文档已保存至" + SaveFileName + "，点击‘查看结果’按钮查看结果。";

               }
           }

           private void button_result_Click(object sender, EventArgs e)
           {
               var enc = Encoding.GetEncoding("GB18030");
               FileStream File = new FileStream(SaveFileName, FileMode.Open);
               StreamReader sr = new StreamReader(File, enc, true);
               result.Text = sr.ReadToEnd();
               File.Close();
               
           }

           private void button1_Click_1(object sender, EventArgs e)
           {

               var enc = Encoding.GetEncoding("GB18030");
               FileStream File = new FileStream(SaveFileName, FileMode.Open);
               StreamReader sr = new StreamReader(File, enc, true);
               string search_result = "";
               string search_line; 
               while((search_line=sr.ReadLine())!=null){
                   if(search_line.Contains(keyword_search.Text))
                        search_result+=search_line+"\r\n";
               }
               File.Close();
               result.Text = search_result;
               
           }

           private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
           {

           }

           private void saveFileDialog1_FileOk(object sender, CancelEventArgs e)
           {

           }

           private void button_savedir_Click(object sender, EventArgs e)
           {
               SaveFileDialog sfd = new SaveFileDialog();
              // sfd.Filter = "txt files(*.txt)";
               sfd.RestoreDirectory = true;
               if (sfd.ShowDialog() == DialogResult.OK)
               {
                   SaveFileName = sfd.FileName.ToString();
               }
           }
    }
}
