##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install socat
#
# You can edit this file again by typing:
#
#     spack edit socat
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Socat(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://www.dest-unreach.org/socat/download/socat-2.0.0-b9.tar.gz"

    version('2.0.0-b9', '5b05b7b86f073a133f7c7aaa453de280')
    version('2.0.0-b8', 'df6a7b2df93fa487be17649fd11dd6fc')
    version('1.7.3.2',  'aec3154f7854580cfab0c2d81e910519')
    version('1.7.3.1',  'fbab6334919cbd71433213db18dbbdf0')
    version('1.7.3.0',  'de46e3f726f783271226eb94d5109bf8')
    version('1.7.2.4',  '2a15dc3362f49d543abdbacc267d0a41')
    version('1.7.1.3',  'f5cd212c511725864c4b5e08a22d3366')
    version('1.7.0.1',  '08cb551967f542b11816fa8c03bf1a00')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
