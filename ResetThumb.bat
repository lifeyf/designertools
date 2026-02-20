@echo off
echo 正在清理缩略图缓存...
taskkill /f /im explorer.exe

:: 清理缩略图缓存数据库
del /f /s /q "%LocalAppData%\Microsoft\Windows\Explorer\thumbcache_*.db"

:: 清理图标缓存数据库
del /f /s /q "%LocalAppData%\IconCache.db"

echo 正在恢复资源管理器...
start explorer.exe

echo 缓存刷新完成！
pause