Cabot MSTeams Plugin
=====

This is an alert plugin for the cabot service monitoring tool. It allows you to alert users by their user handle in a MS Teams channel.

## Installation
Enter the cabot virtual environment.
- sudo pip install https://github.com/prinzpiuz/cabot_alert_msteams.git
- foreman stop
- Add cabot_alert_msteams to the installed apps in settings.py
- foreman run python manage.py syncdb
- foreman start
