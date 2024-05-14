import py2exe

py2exe.freeze(
    windows=[{"script": "main.pyw", "dest_base": "image-notes"}],
    options={"bundle_files": 1}
)
