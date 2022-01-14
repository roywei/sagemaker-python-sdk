# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""Accessors to retrieve the model artifact S3 URI of pretrained ML models."""
from __future__ import absolute_import

import logging
from typing import Optional

from sagemaker.jumpstart import utils as jumpstart_utils
from sagemaker.jumpstart import artifacts


logger = logging.getLogger(__name__)


def retrieve(
    region=None,
    model_id=None,
    model_version: Optional[str] = None,
    model_scope: Optional[str] = None,
) -> str:
    """Retrieves the model artifact S3 URI for the model matching the given arguments.

    Args:
        region (str): Region for which to retrieve model S3 URI.
        model_id (str): JumpStart model ID of the JumpStart model for which to retrieve
            the model artifact S3 URI.
        model_version (str): Version of the JumpStart model for which to retrieve
            the model artifact S3 URI.
        model_scope (str): The model type, i.e. what it is used for.
            Valid values: "training" and "inference".
    Returns:
        str: the model artifact S3 URI for the corresponding model.

    Raises:
        ValueError: If the combination of arguments specified is not supported.
    """
    if not jumpstart_utils.is_jumpstart_model_input(model_id, model_version):
        raise ValueError("Must specify `model_id` and `model_version` when retrieving script URIs.")

    # mypy type checking require these assertions
    assert model_id is not None
    assert model_version is not None

    return artifacts._retrieve_model_uri(model_id, model_version, model_scope, region)