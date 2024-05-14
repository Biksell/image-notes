import py2exe

py2exe.freeze(
    console=[{"script": "main.pyw", "dest_base": "image_notes"}],
    zipfile="req.zip",
    data_files=[("", "res")],
    options={"bundle_files": 2}
)
