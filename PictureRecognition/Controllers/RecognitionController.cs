using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using PictureRecognition.Helper;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace PictureRecognition.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class RecognitionController : ControllerBase
    {        
        public static IHostingEnvironment _environment;
        string pathProgram = @"E:\Coursework\PictureRecognition\PictureRecognitionApp\PictureRecognitionApp";

        private readonly ILogger<RecognitionController> _logger;

        public RecognitionController(ILogger<RecognitionController> logger, IHostingEnvironment environment)
        {
            _logger = logger;
            _environment = environment;
        }

        [HttpGet]
        public string Get()
        {
            int fCount = Directory.GetFiles(_environment.ContentRootPath + "\\uploads\\").Length;
            return $"Images count = {fCount.ToString()}";
        }

        [HttpPost("PredictText")]
        public async Task<string> PredictText(IFormCollection collection)
        {
            var files = collection.Files;
            string pathProgram = @"E:\Coursework\PictureRecognition\NeironNetwork";
            if (files.Count > 0)
            {
                try
                {
                    if (!Directory.Exists(pathProgram + "\\uploads\\"))
                    {
                        Directory.CreateDirectory(pathProgram + "\\uploads\\");
                    }
                    using (FileStream filestream = System.IO.File.Create(pathProgram + "\\uploads\\" + files.FirstOrDefault().FileName,((int)FileOptions.Asynchronous)))
                    {
                        files.FirstOrDefault().CopyTo(filestream);
                        filestream.Flush();
                        //return "\\uploads\\" + files.FirstOrDefault().FileName;                 
                        string filename ="uploads\\" + files.FirstOrDefault().FileName;
                        string result = ScriptRunner.RunFromCmd(@"E:\Coursework\PictureRecognition\NeironNetwork\api_letters.py", filename);
                        return result;
                    }
                }
                catch (Exception ex)
                {
                    return ex.ToString();
                }
            }
            else
            {
                return "Unsuccessful";
            }
        }
        [HttpPost("PredictImage")]
        public async Task<string> PredictImage(IFormCollection collection)
        {
            var files = collection.Files;
            if (files.Count > 0)
            {
                try
                {                    
                    if (!Directory.Exists(pathProgram + "\\uploads\\"))
                    {
                        Directory.CreateDirectory(pathProgram + "\\uploads\\");
                    }
                    using (FileStream filestream = System.IO.File.Create(pathProgram + "\\uploads\\" + files.FirstOrDefault().FileName))
                    {
                        files.FirstOrDefault().CopyTo(filestream);
                        filestream.Flush();
          
                        string filename = "uploads\\" + files.FirstOrDefault().FileName;
                        string result = ScriptRunner.RunFromCmd(@"E:\Coursework\PictureRecognition\NeironNetwork\api_image.py", filename);
                        return result;
                    }
                }
                catch (Exception ex)
                {
                    return ex.ToString();
                }
            }
            else
            {
                return "Unsuccessful";
            }
        }
        [HttpPost("GetImages")]
        public async Task<string> GetImages(IFormCollection collection)
        {
            var files = collection.Files;
            string pathProgram = @"E:\Coursework\PictureRecognition\NeironNetwork";
            if (files.Count > 0)
            {
                try
                {
                    if (!Directory.Exists(pathProgram + "\\uploads\\divided\\"))
                    {
                        Directory.CreateDirectory(pathProgram + "\\uploads\\divided\\");
                    }
                    using (FileStream filestream = System.IO.File.Create(pathProgram + "\\uploads\\divided\\" + files.FirstOrDefault().FileName))
                    {
                        files.FirstOrDefault().CopyTo(filestream);
                        filestream.Flush();

                        string filename = "uploads\\divided\\" + files.FirstOrDefault().FileName;
                        string result = ScriptRunner.RunFromCmd(@"E:\Coursework\PictureRecognition\NeironNetwork\api_images.py", filename);
                        return result;
                    }
                }
                catch (Exception ex)
                {
                    return ex.ToString();
                }
            }
            else
            {
                return "Unsuccessful";
            }
        }

        [HttpPost("GetImageClasses")]
        public async Task<string> GetImageClasses(IFormCollection collection)
        {
            var files = collection.Files;
            if (files.Count > 0)
            {
                try
                {
                    if (!Directory.Exists(pathProgram + "\\uploads\\divided\\"))
                    {
                        Directory.CreateDirectory(pathProgram + "\\uploads\\divided\\");
                    }
                    using (FileStream filestream = System.IO.File.Create(pathProgram + "\\uploads\\divided\\" + files.FirstOrDefault().FileName))
                    {
                        files.FirstOrDefault().CopyTo(filestream);
                        filestream.Flush();

                        string filename = "uploads\\divided\\" + files.FirstOrDefault().FileName;
                        string result = ScriptRunner.RunFromCmd(@"E:\Coursework\PictureRecognition\NeironNetwork\api_image_classes.py", filename);
                        return result;
                    }
                }
                catch (Exception ex)
                {
                    return ex.ToString();
                }
            }
            else
            {
                return "Unsuccessful";
            }
        }

        [HttpPost("GetImageClassesSymbols")]
        public async Task<string> GetImageClassesSymbols(IFormCollection collection)
        {
            var files = collection.Files;
            if (files.Count > 0)
            {
                try
                {
                    if (!Directory.Exists(pathProgram + "\\uploads\\"))
                    {
                        Directory.CreateDirectory(pathProgram + "\\uploads\\");
                    }
                    using (FileStream filestream = System.IO.File.Create(pathProgram + "\\uploads\\" + files.FirstOrDefault().FileName))
                    {
                        files.FirstOrDefault().CopyTo(filestream);
                        filestream.Flush();

                        string filename = "uploads\\" + files.FirstOrDefault().FileName;
                        string result = ScriptRunner.RunFromCmd(@"E:\Coursework\PictureRecognition\NeironNetwork\api_image_classes_symbols.py", filename);
                        return result;
                    }
                }
                catch (Exception ex)
                {
                    return ex.ToString();
                }
            }
            else
            {
                return "Unsuccessful";
            }
        }
    }
}
