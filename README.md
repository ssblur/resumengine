# ResumEngine

## What is ResumEngine?
This is a personal project of mine intended as both a portfolio piece and a way to organize my portfolio.

This is a plugin for a server using Django, which can tag various kinds of portfolio pieces, resume information, and more, and display them on a page for prospective employers easily.

## Installation
Installation is relatively simple, however this application is not currently posted on any Python repositories, so must be installed manually. Instructions are below.

 - Have Python 3.
 - Create a Django project.
 - Add this repository as a directory in your project.
 - Use pip to install all the requirements for this project (`python -m pip install -r requirements.txt`).
 - In settings.py, add the following to the default INSTALLED_APPS: `'portfolio', 'bootstrap4', 'markdownify'`.
 - Configure your MEDIA_URL and MEDIA_ROOT in settings.py.
 - In the root urls.py, add a static route to media/icons (such as `urlpatterns += static(join(settings.MEDIA_URL, 'icons'), document_root=join(settings.MEDIA_ROOT, 'icons'))`).
 - Run the manage.py `migrate` task.
 - (Optional, but recommended) Test using manage.py's `runserver` task.
 - Run your server using your preferred menu.

Apologies for the somewhat complex setup, this project was created, for the most part, in a few hours.

## Technologies Used
This is a Django plugin. Docker may be used in the future for containerization.

## License

GPLv3. A copy is included in [LICENSE](LICENSE), or you can find it online [here](https://www.gnu.org/licenses/gpl-3.0.en.html).