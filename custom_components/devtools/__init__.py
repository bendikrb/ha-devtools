import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_TOKEN
from homeassistant.core import (
    HomeAssistant,
    ServiceCall,
    ServiceResponse,
    SupportsResponse,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.network import get_url

from .const import DOMAIN
from .ha_connection import HAConnection

_LOGGER = logging.getLogger(__package__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up devtools from a config entry."""

    access_token = entry.data[CONF_TOKEN]
    web_session = async_get_clientsession(hass)

    async def handle_call_ws_endpoint(call: ServiceCall) -> ServiceResponse:
        ws_type = call.data.get("type")
        ws_data = call.data.get("data", {})

        message = {"type": ws_type, **ws_data}
        async with HAConnection(
            url=get_url(hass),
            token=access_token,
            hass=hass,
            session=web_session,
        ) as sock:
            response = await sock.send_and_receive(message)
            if call.return_response:
                return {
                    "response": response,
                }
            return None

    hass.services.async_register(
        DOMAIN,
        "call_ws_endpoint",
        handle_call_ws_endpoint,
        supports_response=SupportsResponse.OPTIONAL,
    )

    return True
