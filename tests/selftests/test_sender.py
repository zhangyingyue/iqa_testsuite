from amom.client import Sender
from odict import odict



def test_isinstance(sender: Sender):
    """
    Check if created sender is instance of Sender class.
    :param sender:
    """
    assert isinstance(sender, Sender)


def test_name(sender: Sender):
    """
    Check if created sender is available in the test-suite.
    :param sender:
    """
    clients = ['Internal core client','NodeJS RHEA client']
    assert (sender.name in clients) == True


def test_attributes(sender: Sender):
    """
    Check if all internal attributes are created.
    :param sender:
    """
    output = False

    for name, value in sender.cli_params_transformation.items():
        name = sender.attribute_prefix + name
        output = hasattr(sender, name)

    assert output == True