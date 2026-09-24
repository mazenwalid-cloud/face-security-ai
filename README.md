# Face Security AI

> Modular real-time face recognition with Python, OpenCV, and face-recognition.

## Overview

Face Security AI is a computer-vision application that detects and recognizes enrolled faces through a webcam.

The project is organized into separate modules for camera handling, face detection, encoding, matching, local storage, and configuration.

## Features

- Real-time webcam face detection
- Face encoding and identity matching
- Multiple enrolled identities
- Multi-sample enrollment
- Configurable matching threshold
- Modular Python architecture
- Local JSON-based embedding storage

## Architecture

```text
Webcam
  |
  v
Camera Manager
  |
  v
Face Detector
  |
  v
Face Encoder
  |
  v
Face Matcher <--- Face Database
  |
  v
Identity / Unknown
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Application runtime |
| OpenCV | Camera access and face detection |
| face-recognition | Face encoding and comparison |
| NumPy | Numerical operations |
| JSON | Local embedding storage |

## Installation

```bash
git clone https://github.com/mazenwalid-cloud/face-security-ai.git
cd face-security-ai
python -m venv venv
```

Windows PowerShell:

```powershell
.\\venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

## Usage

### Enroll a person

```powershell
cd FaceSecurity
python enroll.py
```

Enter a name and follow the camera prompts.

### Start recognition

```powershell
python main.py
```

Press **Q** to exit.

## Configuration

Edit `FaceSecurity/config/settings.py` to configure:

- `CAMERA_INDEX`
- `WINDOW_NAME`
- `FACE_DATABASE_PATH`
- `FACE_MATCH_THRESHOLD`
- `EXIT_KEY`

The default matching threshold is `0.6` and should be treated as an engineering starting point, not a security guarantee.

## Privacy & Security

This application processes biometric face representations.

- Do not commit real biometric data to a public repository.
- Local face data is excluded through `.gitignore`.
- Production deployments should consider encryption, access control, consent, retention policies, audit logging, and secure storage.

## Limitations

- No liveness / anti-spoofing detection
- Detection can be affected by lighting, pose, and image quality
- Matching is threshold-based
- Local JSON storage is not suitable for high-security production systems
- No encrypted biometric database

## Roadmap

- [x] Face detection
- [x] Face encoding
- [x] Identity matching
- [x] Multi-user enrollment
- [x] Configurable threshold
- [x] Modular architecture
- [ ] Automated tests and CI
- [ ] Liveness / anti-spoofing
- [ ] Encrypted biometric storage
- [ ] Access and event logging

## Developer

**Mazen Walid**  
Junior AI Engineer · Computer Vision

GitHub: https://github.com/mazenwalid-cloud

## License

MIT License. See [LICENSE](LICENSE).
