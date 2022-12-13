using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Swashbuckle.AspNetCore.Swagger;
using Swashbuckle.AspNetCore.SwaggerGen;
using System.Collections.Generic;
using Swashbuckle.Swagger;
using Microsoft.OpenApi.Models;

namespace PictureRecognition.Helpers
{
    

    namespace FileUploadSample
    {
        public class SwaggerFileOperationFilter : Swashbuckle.AspNetCore.SwaggerGen.IOperationFilter
        {
            public void Apply(OpenApiOperation operation, OperationFilterContext context)
            {

                operation.Parameters.Add(
                    new OpenApiParameter
                    {
                        Name = "Files",
                        In = ParameterLocation.Header,
                        Description = "Upload File",
                        Required = true,
                        Schema = new OpenApiSchema
                        {
                            Type = "file",
                            Format = "binary"
                        }
                    }
                );
               
            }
        }
    }
}
