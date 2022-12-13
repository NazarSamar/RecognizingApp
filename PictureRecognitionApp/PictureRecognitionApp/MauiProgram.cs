using Microsoft.AspNetCore.Components.WebView.Maui;
using Microsoft.Maui.LifecycleEvents;
using PictureRecognitionApp.Data;

namespace PictureRecognitionApp;

public static class MauiProgram
{
	public static MauiApp CreateMauiApp()
	{
		var builder = MauiApp.CreateBuilder();
		builder
			.UseMauiApp<App>()
			.ConfigureFonts(fonts =>
			{
				fonts.AddFont("e-Ukraine-Bold.otf", "e-Ukraine-Bold");
                fonts.AddFont("e-Ukraine-Medium.otf", "e-Ukraine-Medium");
                fonts.AddFont("e-Ukraine-Regular.otf", "e-Ukraine-Regular");                                
            });

		builder.Services.AddMauiBlazorWebView();
#if DEBUG
		builder.Services.AddBlazorWebViewDeveloperTools();
#endif

		builder.Services.AddSingleton<ImageService>();

        return builder.Build();
	}
}
