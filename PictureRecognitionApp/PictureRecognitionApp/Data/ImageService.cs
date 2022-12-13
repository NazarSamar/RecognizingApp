namespace PictureRecognitionApp.Data;
using System.Net;
using System.Net.Http.Headers;

public class ImageService
{   

    public async Task<string> sendRequest(string _url, string image_location, string image_name)
    {
        using var client = new HttpClient();
        string url = _url;

        var multipartFormContent = new MultipartFormDataContent();

        File.Copy(image_location, image_location + "_copy", true);

        using (var fs = new FileStream(image_location + "_copy", FileMode.Open, FileAccess.Read))
        using (var fileStreamContent = new StreamContent(fs))
        {
            fileStreamContent.Headers.ContentType = new MediaTypeHeaderValue("image/png");

            multipartFormContent.Add(fileStreamContent, name: "file", fileName: image_name);
            var response = await client.PostAsync(url, multipartFormContent);

            return await response.Content.ReadAsStringAsync();
        }
    }

    private string apiUrl = "http://localhost:53185/Recognition";

    public Task<ImageFile[]> GetImagesAsync()
    {
        var dir = new DirectoryInfo(@"E:\Coursework\PictureRecognition\NeironNetwork\uploads\");
        FileInfo[] files = dir.GetFiles();
        var images = new List<ImageFile>();
        foreach (var file in files)
        {
            var img = new ImageFile() { Name = file.Name, Size = Convert.ToInt32(file.Length) };
            images.Add(img);
        }
        return Task.FromResult(images.ToArray());
    }

    public async Task<string> PredictText(string image_location, string image_name)
    {
        var url = @$"{apiUrl}/PredictText";
        return await sendRequest(url, image_location, image_name);
    }

    public async Task<string> PredictImage(string image_location, string image_name)
    {
        var url = @$"{apiUrl}/PredictImage";
        return await sendRequest(url, image_location, image_name);
    }
    public async Task<string> GetImageClassesSymbols(string image_location, string image_name)
    {
        var url = @$"{apiUrl}/GetImageClassesSymbols";
        return await sendRequest(url, image_location, image_name);
    }

}

