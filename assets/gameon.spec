# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gameon.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\\\Users\\\\6700k\\\\OneDrive\\\\Skrivbord\\\\GAME ON\\\\assets\\\\musik.mp3', '.'), ('C:\\\\Users\\\\6700k\\\\OneDrive\\\\Skrivbord\\\\GAME ON\\\\assets\\\\player.png', '.'), ('C:\\\\Users\\\\6700k\\\\OneDrive\\\\Skrivbord\\\\GAME ON\\\\assets\\\\balls.png', '.'), ('C:\\\\Users\\\\6700k\\\\OneDrive\\\\Skrivbord\\\\GAME ON\\\\assets\\\\kvadrat.png', '.'), ('C:\\\\Users\\\\6700k\\\\OneDrive\\\\Skrivbord\\\\GAME ON\\\\assets\\\\triangel.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='gameon',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
