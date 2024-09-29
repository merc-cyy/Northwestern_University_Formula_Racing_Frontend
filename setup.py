from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["numpy"],
    "zip_include_packages": ["matplotlib"],
}

setup(
    name="formula",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("formula.py", base="gui")],
)