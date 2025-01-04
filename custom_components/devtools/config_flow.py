import voluptuous as vol

from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_TOKEN
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.network import get_url

from .const import DOMAIN
from .exceptions import WebSocketAuthenticationError
from .ha_connection import HAConnection


async def validate_input(hass, data):
    """Validate if the given token allows us to connect."""
    async with HAConnection(
        url=get_url(hass),
        token=data[CONF_TOKEN],
        hass=hass,
        session=async_get_clientsession(hass),
    ) as sock:
        await sock.send_and_receive({"type": "ping"})


class DevToolsConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for devtools."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is None:
            return self._show_setup_form()

        try:
            await validate_input(self.hass, user_input)
        except WebSocketAuthenticationError:
            return self._show_setup_form({"base": "cannot_connect"})

        return self.async_create_entry(title="DevTools", data=user_input)

    def _show_setup_form(self, errors: dict | None = None):
        """Show the setup form to the user."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_TOKEN): str,
                }
            ),
            errors=errors or {},
        )
