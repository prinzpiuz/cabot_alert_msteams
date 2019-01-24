from cabot.cabotapp.tests.tests_basic import LocalTestCase
from mock import Mock, patch

from cabot.cabotapp.models import UserProfile, Service
from cabot_alert_hipchat import models
from cabot.cabotapp.alert import update_alert_plugins

class TestHipchatAlerts(LocalTestCase):
    def setUp(self):
        super(TestHipchatAlerts, self).setUp()

        self.user_profile = UserProfile(user=self.user)
        self.user_profile.save()
        self.hipchat_user_data = models.HipchatAlertUserData.objects.create(
            hipchat_alias = "test_user_hipchat_alias",
            user = self.user_profile,
            title=models.HipchatAlertUserData.name,
            )
        self.hipchat_user_data.save()

        self.service.users_to_notify.add(self.user)

        update_alert_plugins()
        self.hipchat_plugin = models.HipchatAlert.objects.get(title=models.HipchatAlert.name)
        self.service.alerts.add(self.hipchat_plugin)
        self.service.save()
        self.service.update_status()

    def test_users_to_notify(self):
        self.assertEqual(self.service.users_to_notify.all().count(), 1)
        self.assertEqual(self.service.users_to_notify.get(pk=1).username, self.user.username)

    @patch('cabot_alert_hipchat.models.HipchatAlert._send_hipchat_alert')
    def test_normal_alert(self, fake_hipchat_alert):
        self.service.overall_status = Service.PASSING_STATUS
        self.service.old_overall_status = Service.ERROR_STATUS
        self.service.save()
        self.service.alert()
        fake_hipchat_alert.assert_called_with(u'Service Service is back to normal: http://localhost/service/1/. @test_user_hipchat_alias', color='green', sender='Cabot/Service')

    @patch('cabot_alert_hipchat.models.HipchatAlert._send_hipchat_alert')
    def test_failure_alert(self, fake_hipchat_alert):
        # Most recent failed
        self.service.overall_status = Service.CALCULATED_FAILING_STATUS
        self.service.old_overall_status = Service.PASSING_STATUS
        self.service.save()
        self.service.alert()
        fake_hipchat_alert.assert_called_with(u'Service Service reporting failing status: http://localhost/service/1/. Checks failing: @test_user_hipchat_alias', color='red', sender='Cabot/Service')
