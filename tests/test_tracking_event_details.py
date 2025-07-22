from datetime import datetime

from openfeature.tracking_event_details import TrackingEventDetails


# Specification("6.2.1", "The `tracking event details` structure MUST define an optional numeric `value`, associating a scalar quality with an `tracking event`.")
def test_optional_value_property():
    details = TrackingEventDetails()
    assert details.value is None


# Specification("6.2.1", "The `tracking event details` structure MUST define an optional numeric `value`, associating a scalar quality with an `tracking event`.")
def test_has_value_property():
    value = 23.5
    details = TrackingEventDetails(value)
    assert details.value is value


# Specification("6.2.2", "The `tracking event details` MUST support the inclusion of custom fields, having keys of type `string`, and values of type `boolean | string | number | structure`.")
def test_can_take_values():
    structure = {"key", "value"}
    date_time_value = datetime.now()
    details = (
        TrackingEventDetails()
        .add("boolean", True)
        .add("string", "some string")
        .add("double", 123.3)
        .add("structure", structure)
        .add("value", date_time_value)
    )

    assert details.get("boolean") is True
    assert details.get("string") == "some string"
    assert details.get("double") == 123.3
    assert details.get("structure") is structure
    assert details.get("value") is date_time_value
