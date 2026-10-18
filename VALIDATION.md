# Validation

Validated on Windows on October 18, 2026:

- All 1,131 upstream files match their recorded Git blob IDs and SHA-256 hashes.
- The original research note is byte-identical to the supplied attachment.
- Teardown's authored local reference links resolve and its skill entrypoint
  passes the skill validator.
- Independent routing checks reached seven specialist workflows, including REA
  JavaScript analysis, Unity mod porting, crash triage and PS5 compatibility work.
- Twenty offline helper checks passed, covering download integrity, archive path
  guards, cache reuse, ARM64 runtime selection, runtime-probe fallback, JDK reuse,
  local resource resolution and literal subprocess arguments.
- REA 6.7.0 installed through the helper and statically analyzed a three-file
  JavaScript fixture with zero parse failures. No target code was executed.
- Universal Modder installed into a private virtual environment and successfully
  searched its bundled Unity knowledge.

The mocked platform checks do not establish native execution on every OS or
architecture. Ghidra, JADX, ILSpy, Cpp2IL, licensed IDA and PS5 builds were not
installed or executed during this validation. Windows Ghidra/JADX setup supplies
paths for provider configuration; generic helper execution declines batch files.

## Reproduce the repository checks

```sh
python3 maintenance/verify_bundle.py
python3 tests/check_helpers.py
python3 maintenance/package.py
```

Use `py -3` on Windows if that is your Python launcher. The checks do not download
or install tools. Helper results are written under `.artifacts/helper-checks/`;
the generated ZIP and checksum go under `dist/`. These outputs are ignored by Git.

GitHub Actions repeats the bundle and helper checks on Windows and Linux. Its
current run status is the evidence for those environments; an unexecuted
workflow definition is not a passing result.
