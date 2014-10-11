@Thanks to https://gist.github.com/georgevreilly/8444988
@REM adapted from http://stackoverflow.com/a/20092578
if ["%VIRTUAL_ENV%"]==[""] echo Must run under a Virtualenv && goto :error
 
set SRCDIR=c:\Python27\Lib\site-packages
pushd "%VIRTUAL_ENV%\Lib\site-packages"
xcopy /ydfsi %SRCDIR%\MySQLdb MySQLdb
xcopy /ydfsi %SRCDIR%\_mysql* .
xcopy /ydfsi %SRCDIR%\MySQL_python-1.2.3-py2.7.egg-info MySQL_python-1.2.3-py2.7.egg-info
popd
goto :eof
 
:error
exit /b 1
goto :eof