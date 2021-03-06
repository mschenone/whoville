# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SharedServiceResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'shared_cluster_name': 'str',
        'shared_cluster_id': 'int',
        'attached_clusters': 'list[AttachedClusterInfoResponse]'
    }

    attribute_map = {
        'shared_cluster_name': 'sharedClusterName',
        'shared_cluster_id': 'sharedClusterId',
        'attached_clusters': 'attachedClusters'
    }

    def __init__(self, shared_cluster_name=None, shared_cluster_id=None, attached_clusters=None):
        """
        SharedServiceResponse - a model defined in Swagger
        """

        self._shared_cluster_name = None
        self._shared_cluster_id = None
        self._attached_clusters = None

        if shared_cluster_name is not None:
          self.shared_cluster_name = shared_cluster_name
        if shared_cluster_id is not None:
          self.shared_cluster_id = shared_cluster_id
        if attached_clusters is not None:
          self.attached_clusters = attached_clusters

    @property
    def shared_cluster_name(self):
        """
        Gets the shared_cluster_name of this SharedServiceResponse.

        :return: The shared_cluster_name of this SharedServiceResponse.
        :rtype: str
        """
        return self._shared_cluster_name

    @shared_cluster_name.setter
    def shared_cluster_name(self, shared_cluster_name):
        """
        Sets the shared_cluster_name of this SharedServiceResponse.

        :param shared_cluster_name: The shared_cluster_name of this SharedServiceResponse.
        :type: str
        """

        self._shared_cluster_name = shared_cluster_name

    @property
    def shared_cluster_id(self):
        """
        Gets the shared_cluster_id of this SharedServiceResponse.

        :return: The shared_cluster_id of this SharedServiceResponse.
        :rtype: int
        """
        return self._shared_cluster_id

    @shared_cluster_id.setter
    def shared_cluster_id(self, shared_cluster_id):
        """
        Sets the shared_cluster_id of this SharedServiceResponse.

        :param shared_cluster_id: The shared_cluster_id of this SharedServiceResponse.
        :type: int
        """

        self._shared_cluster_id = shared_cluster_id

    @property
    def attached_clusters(self):
        """
        Gets the attached_clusters of this SharedServiceResponse.

        :return: The attached_clusters of this SharedServiceResponse.
        :rtype: list[AttachedClusterInfoResponse]
        """
        return self._attached_clusters

    @attached_clusters.setter
    def attached_clusters(self, attached_clusters):
        """
        Sets the attached_clusters of this SharedServiceResponse.

        :param attached_clusters: The attached_clusters of this SharedServiceResponse.
        :type: list[AttachedClusterInfoResponse]
        """

        self._attached_clusters = attached_clusters

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SharedServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
