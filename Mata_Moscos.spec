# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Mata_Moscos.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\drluc\\anaconda3\\envs\\JuegoErick\\Lib\\site-packages\\mediapipe\\modules\\palm_detection\\palm_detection_full.tflite', 'mediapipe/modules/palm_detection'), ('C:\\Users\\drluc\\anaconda3\\envs\\JuegoErick\\Lib\\site-packages\\mediapipe\\modules\\hand_landmark\\hand_landmark_tracking_cpu.binarypb', 'mediapipe/modules/hand_landmark'), ('C:\\Users\\drluc\\anaconda3\\envs\\JuegoErick\\Lib\\site-packages\\mediapipe\\modules\\hand_landmark\\hand_landmark_full.tflite', 'mediapipe/modules/hand_landmark'), ('C:\\Users\\drluc\\anaconda3\\envs\\JuegoErick\\Lib\\site-packages\\mediapipe\\modules\\hand_landmark\\handedness.txt', 'mediapipe/modules/hand_landmark')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Mata_Moscos',
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
    icon=['C:\\Users\\drluc\\OneDrive\\Escritorio\\Codigos Pruebas\\FeriaDeLibro\\Juegos\\JuegoErick\\MataMoscos\\icono.ico'],
)
