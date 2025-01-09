# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Libnabo(CMakePackage):
    """libnabo is a fast K Nearest Neighbour library for low-dimensional spaces"""

    homepage = "https://github.com/ethz-asl/libnabo"
    url      = "https://github.com/ethz-asl/libnabo"
    git      = "https://github.com/ethz-asl/libnabo"

    version('1.0.7', tag='1.0.7')
    version('master', branch='master')

    depends_on('eigen')

    #def cmake_args(self):
    #    args = ['-DCMAKE_C_COMPILER=%s' % self.spec['mpi'].mpicc,
    #            '-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx]
    #    return args
