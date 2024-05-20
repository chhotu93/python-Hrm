from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver

baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
username = "Admin"
password = "admin123"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    # driver = webdriver.Chrome()
    request.cls.driver = webdriver.Chrome()
    # yield
    # driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("hrmreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    # html = report_dir / f"Report_{'%Y%m%d%H%M'}.html"
    html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Hrm Test report"
