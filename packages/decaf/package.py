# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Decaf(CMakePackage):
    """A dataflow system for the parallel communication of coupled tasks in an HPC workflow."""

    homepage = "https://tpeterka.github.io/decaf/"
    url      = "https://github.com/tpeterka/decaf.git"
    git      = "https://github.com/tpeterka/decaf.git"

    version('master', branch='master')
    version('mraj', git='https://github.com/hguo/decaf.git')

    depends_on('mpi')
    depends_on('boost')
    depends_on('python@3:',   type='run')
    depends_on('py-networkx', type='run')

    depends_on('netcdf-c@4.6.1 +mpi', type='link', when='@mraj')
    depends_on('vtk', type='link', when='@mraj')
    depends_on('parallel-netcdf@1.7.0 -shared', type='link', when='@mraj')
    depends_on('libnabo', type='link', when='@mraj')
    depends_on('diy', type='link', when='@mraj')

    def cmake_args(self):
        args = ['-DCMAKE_C_COMPILER=%s' % self.spec['mpi'].mpicc,
                '-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx]

        if (self.spec.satisfies('@mraj')):
            args.append('-DDIY_INCLUDE_DIRS={0}'.format(self.spec['diy'].prefix.include))

        return args
