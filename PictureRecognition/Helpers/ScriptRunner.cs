using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PictureRecognition.Helper
{
    public static class ScriptRunner
    {
        //args separated by spaces
        public static string RunFromCmd(string rCodeFilePath, string args)
        {
            string file = rCodeFilePath;
            string result = string.Empty;
            System.Text.Encoding.RegisterProvider(System.Text.CodePagesEncodingProvider.Instance);
            try
            {

                var info = new ProcessStartInfo(@"E:\Anaconda\envs\nenv\python.exe");
                info.Arguments = rCodeFilePath + " " + args;

                info.RedirectStandardInput = false;
                info.RedirectStandardOutput = true;
                info.UseShellExecute = false;
                info.CreateNoWindow = true;
                info.StandardOutputEncoding = Encoding.GetEncoding(21866);

                using (var proc = new Process())
                {
                    proc.StartInfo = info;
                    proc.Start();
                    proc.WaitForExit();
                   
                    result = proc.StandardOutput.ReadToEnd();
                    
                }
                return result;
            }
            catch (Exception ex)
            {
                throw new Exception("R Script failed: " + result, ex);
            }
        }
    }
}
