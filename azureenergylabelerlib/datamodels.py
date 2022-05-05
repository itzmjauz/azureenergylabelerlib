#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: azureenergylabelerlib.py
#
# Copyright 2022 Sayantan Khanra
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
Main code for azureenergylabelerlib.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import logging
import json

__author__ = '''Sayantan Khanra <skhanra@schubergphilis.com>'''
__docformat__ = '''google'''
__date__ = '''22-04-2022'''
__copyright__ = '''Copyright 2022, Sayantan Khanra'''
__credits__ = ["Sayantan Khanra"]
__license__ = '''MIT'''
__maintainer__ = '''Sayantan Khanra'''
__email__ = '''<skhanra@schubergphilis.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".

# This is the main prefix used for logging
LOGGER_BASENAME = '''datamodels'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())


class TenantEnergyLabelingData:  # pylint: disable=too-few-public-methods
    """Models the data for energy labeling to export."""

    def __init__(self,
                 filename,
                 id,  # pylint: disable= redefined-builtin
                 energy_label):
        self.filename = filename
        self._id = id
        self._energy_label = energy_label

    @property
    def json(self):
        """Data to json."""
        return json.dumps([{'Tenant ID': self._id,
                            'Tenant Energy Label': self._energy_label}],
                          indent=2, default=str)


class DefenderForCloudFindingsData:  # pylint: disable=too-few-public-methods
    """Models the data for energy labeling to export."""

    def __init__(self, filename, defender_for_cloud_findings):
        self.filename = filename
        self._defender_for_cloud_findings = defender_for_cloud_findings

    @property
    def json(self):
        """Data to json."""
        return json.dumps([{'Compliance Standard ID': finding.compliance_standard_id,
                            'Compliance Control ID': finding.compliance_control_id,
                            'Compliance State': finding.compliance_state,
                            'Subscription ID': finding.subscription_id,
                            'Resource Group': finding.resource_group,
                            'Resource Type': finding.resource_type,
                            'Resource Name': finding.resource_name,
                            'Resource ID': finding.resource_id,
                            'Severity': finding.severity,
                            'State': finding.state,
                            'Recommendation ID': finding.recommendation_id,
                            'Recommendation Name': finding.recommendation_name,
                            'Recommendation Display Name': finding.recommendation_display_name,
                            'Description': finding.description,
                            'Remediation Steps': finding.remediation_steps,
                            'Azure Portal Recommendation Link': finding.azure_portal_recommendation_link,
                            'Control Name': finding.control_name
                            }
                           for finding in self._defender_for_cloud_findings], indent=2, default=str)


class LabeledSubscriptionData:  # pylint: disable=too-few-public-methods
    """Models the data for energy labeling to export."""

    def __init__(self, filename, labeled_subscription):
        self.filename = filename
        self._labeled_subscription = labeled_subscription

    @property
    def data(self):
        """Data of an subscription to export."""
        return {'Subscription ID': self._labeled_subscription.subscription_id,
                'Subscription Display Name': self._labeled_subscription.display_name,
                'Number of high findings':
                    self._labeled_subscription.energy_label.number_of_high_findings,
                'Number of medium findings': self._labeled_subscription.energy_label.number_of_medium_findings,
                'Number of low findings': self._labeled_subscription.energy_label.number_of_low_findings,
                'Energy Label': self._labeled_subscription.energy_label.label}


class LabeledResourceGroupData:
    """Models the data for energy labeling to export."""

    def __init__(self, filename, labeled_resource_group):
        self.filename = filename
        self._labeled_resource_group = labeled_resource_group

    @property
    def data(self):
        """Data of an subscription to export."""
        return {'ResourceGroup Name': self._labeled_resource_group.name,
                'Number of high findings':
                    self._labeled_resource_group.energy_label.number_of_high_findings,
                'Number of medium findings': self._labeled_resource_group.energy_label.number_of_medium_findings,
                'Number of low findings': self._labeled_resource_group.energy_label.number_of_low_findings,
                'Energy Label': self._labeled_resource_group.energy_label.label}

    @property
    def json(self):
        """Data to json."""
        return json.dumps(self.data, indent=2, default=str)


class LabeledSubscriptionsData:  # pylint: disable=too-few-public-methods
    """Models the data for energy labeling to export."""

    def __init__(self, filename, labeled_subscriptions):
        self.filename = filename
        self._labeled_subscriptions = labeled_subscriptions

    @property
    def json(self):
        """Data to json."""
        return json.dumps([LabeledSubscriptionData(self.filename, account).data
                           for account in self._labeled_subscriptions], indent=2, default=str)
