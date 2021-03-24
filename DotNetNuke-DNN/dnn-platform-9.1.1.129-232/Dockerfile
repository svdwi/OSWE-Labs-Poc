# escape=`

FROM microsoft/dotnet-framework:4.7.1-windowsservercore-1709

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

RUN Add-WindowsFeature Web-Server; `
    Add-WindowsFeature NET-Framework-45-ASPNET; `
    Add-WindowsFeature Web-Asp-Net45; `
    Remove-Item -Recurse C:\inetpub\wwwroot\*; `    
    Invoke-WebRequest https://dotnetbinaries.blob.core.windows.net/servicemonitor/2.0.1.1/ServiceMonitor.exe -OutFile C:\ServiceMonitor.exe

# Download Roslyn nupkg and ngen the compiler binaries
RUN [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; ` 
    Invoke-WebRequest -Uri https://api.nuget.org/packages/microsoft.net.compilers.2.3.1.nupkg -OutFile C:\microsoft.net.compilers.2.3.1.zip ; `	
    Expand-Archive -Path c:\microsoft.net.compilers.2.3.1.zip -DestinationPath c:\RoslynCompilers ; `
    Remove-Item c:\microsoft.net.compilers.2.3.1.zip -Force ; `
    &C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngen.exe install c:\RoslynCompilers\tools\csc.exe /ExeConfig:c:\RoslynCompilers\tools\csc.exe | `
    &C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngen.exe install c:\RoslynCompilers\tools\vbc.exe /ExeConfig:c:\RoslynCompilers\tools\vbc.exe  | `
    &C:\Windows\Microsoft.NET\Framework64\v4.0.30319\ngen.exe install c:\RoslynCompilers\tools\VBCSCompiler.exe /ExeConfig:c:\RoslynCompilers\tools\VBCSCompiler.exe | `
    &C:\Windows\Microsoft.NET\Framework\v4.0.30319\ngen.exe install c:\RoslynCompilers\tools\csc.exe /ExeConfig:c:\RoslynCompilers\tools\csc.exe | `
    &C:\Windows\Microsoft.NET\Framework\v4.0.30319\ngen.exe install c:\RoslynCompilers\tools\vbc.exe /ExeConfig:c:\RoslynCompilers\tools\vbc.exe | `
    &C:\Windows\Microsoft.NET\Framework\v4.0.30319\ngen.exe install c:\RoslynCompilers\tools\VBCSCompiler.exe  /ExeConfig:c:\RoslynCompilers\tools\VBCSCompiler.exe ;

ENV ROSLYN_COMPILER_LOCATION c:\\RoslynCompilers\\tools

# Copy DNN files and add permissions
RUN [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; `
    Invoke-WebRequest -Uri https://github.com/dnnsoftware/Dnn.Platform/releases/download/v9.1.0/DNN_Platform_9.1.0.367_Install.zip -OutFile C:\DNN_Platform_9.1.0.367_Install.zip ; `
    Expand-Archive -Path C:\DNN_Platform_9.1.0.367_Install.zip -DestinationPath C:\inetpub\wwwroot\ ; `
    Remove-Item C:\DNN_Platform_9.1.0.367_Install.zip -Force ; `
    cmd /c icacls c:\inetpub\wwwroot /grant 'IIS AppPool\DefaultAppPool:(OI)(CI)M' /T ;

EXPOSE 80

ENTRYPOINT ["C:\\ServiceMonitor.exe", "w3svc"]
