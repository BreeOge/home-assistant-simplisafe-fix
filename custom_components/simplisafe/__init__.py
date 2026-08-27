"""Temporary SimpliSafe dependency override.

Delegate the integration implementation to Home Assistant Core while this
custom component supplies a newer simplisafe-python requirement.
"""

from homeassistant.components.simplisafe import (  # noqa: F401
    SimpliSafe,
    SimpliSafeConfigEntry,
    async_setup,
    async_setup_entry,
    async_unload_entry,
)
