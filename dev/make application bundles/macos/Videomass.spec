# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['videomass'],
             pathex=['/Users/gianluca/Bin/Videomass'],
             binaries=[],
             datas=[('/Users/gianluca/Bin/Videomass/videomass3/art', 'art'), 
                    ('/Users/gianluca/Bin/Videomass/videomass3/locale', 'locale'), 
                    ('/Users/gianluca/Bin/Videomass/videomass3/share', 'share'), 
                    ('/Users/gianluca/Bin/Videomass/MacOsxSetup/FFMPEG_BIN', 'FFMPEG_BIN'), 
                    ('/Users/gianluca/Bin/Videomass/AUTHORS', 'DOC'), 
                    ('/Users/gianluca/Bin/Videomass/BUGS', 'DOC'), 
                    ('/Users/gianluca/Bin/Videomass/CHANGELOG', 'DOC'), 
                    ('/Users/gianluca/Bin/Videomass/COPYING', 'DOC'), 
                    ('/Users/gianluca/Bin/Videomass/INSTALL', 'DOC'), 
                    ('/Users/gianluca/Bin/Videomass/README.md', 'DOC'), 
                    ('/Users/gianluca/Bin/Videomass/TODO', 'DOC')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['youtube_dl'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Videomass',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='/Users/gianluca/Bin/Videomass/videomass3/art/videomass.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Videomass')
app = BUNDLE(coll,
             name='Videomass.app',
             icon='/Users/gianluca/Bin/Videomass/videomass3/art/videomass.icns',
             bundle_identifier='com.jeanslack.videomass',
             info_plist={
                   # 'LSEnvironment': '$0',
                   'NSPrincipalClass': 'NSApplication',
                   'NSAppleScriptEnabled': False,
                   'CFBundleName': 'Videomass',
                   'CFBundleDisplayName': 'Videomass',
                   'CFBundleGetInfoString': "Making Videomass",
                   'CFBundleIdentifier': "com.jeanslack.videomass",
                   'CFBundleVersion': '1.6.1',
                   'CFBundleShortVersionString': '1.6.1',
                   'NSHumanReadableCopyright': 'Copyright © 2013-2019, '
                                            'Gianluca Pernigotto, '
                                            'All Rights Reserved',
                                            }
                        )
