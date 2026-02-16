import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from app.main import app
import os

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def mock_startup():
    # Evita que o startup tente conectar ao banco real
    with patch("app.main.init_db") as mock:
        yield mock

@pytest.fixture
def mock_db():
    # Patch it where it's used to avoid import timing issues
    with patch("app.routes.jobs.get_db_connection") as mock:
        yield mock

@pytest.fixture
def mock_moviepy():
    # Patch direct imports in the route module
    with patch("app.routes.video.VideoFileClip") as v_mock, \
         patch("app.routes.video.AudioFileClip") as a_mock, \
         patch("app.routes.video.ImageClip") as i_mock, \
         patch("app.routes.video.TextClip") as t_mock, \
         patch("app.routes.video.CompositeVideoClip") as comp_mock, \
         patch("app.routes.video.concatenate_videoclips") as concat_mock, \
         patch("moviepy.editor.ColorClip") as c_mock:
        
        # Configure magic mocks to behave like clips
        for m in [v_mock, a_mock, i_mock, t_mock, c_mock]:
            mock_inst = m.return_value
            mock_inst.w = 1920
            mock_inst.h = 1080
            mock_inst.duration = 10.0
            mock_inst.set_duration.return_value = mock_inst
            mock_inst.set_start.return_value = mock_inst
            mock_inst.set_end.return_value = mock_inst
            mock_inst.set_position.return_value = mock_inst
            mock_inst.resize.return_value = mock_inst
            mock_inst.crop.return_value = mock_inst
            mock_inst.without_audio.return_value = mock_inst
        
        yield {
            "video": v_mock,
            "audio": a_mock,
            "image": i_mock,
            "text": t_mock,
            "color": c_mock,
            "composite": comp_mock,
            "concatenate": concat_mock
        }

@pytest.fixture
def mock_fs():
    # Patch where used to avoid issues with pathlib/os mix
    with patch("app.routes.video.os.path.exists") as exists_mock, \
         patch("app.routes.video.os.makedirs") as mkdirs_mock, \
         patch("app.routes.video.os.listdir") as listdir_mock, \
         patch("app.routes.video.os.path.getsize", return_value=1024*1024):
        yield {
            "exists": exists_mock,
            "makedirs": mkdirs_mock,
            "listdir": listdir_mock
        }
