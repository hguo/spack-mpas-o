# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class Pio(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url      = "https://github.com/NCAR/ParallelIO/archive/refs/tags/pio1_7_2.tar.gz"

    maintainers = ['tkameyama']

    version('1_7_2', 'ecc9b50e2c75f0189c76917a555aee3b6dc3cc5e38232007577c51bb2c977e39')

    depends_on('mpi')
    #depends_on('netcdf-c +mpi', type='link')
    #depends_on('netcdf-fortran', type='link')
    depends_on('parallel-netcdf', type='link')

    phases = ['configure', 'build', 'install']

    def configure_args(self):
        spec = self.spec
        prefix = self.prefix

        config_args = [
                '--prefix={0}'.format(prefix),
                '--disable-netcdf',
                '--disable-mpiio',
                'FFLAGS={0}'.format('-mcmodel=medium'),
                #'NETCDF_PATH=' + self.spec['netcdf-fortran'].prefix,
                'PNETCDF_PATH=' + self.spec['parallel-netcdf'].prefix]

        return config_args

    def configure(self, spec, prefix):
        with working_dir('pio'):
            configure = Executable('./configure')
            configure(*self.configure_args())

    def build(self, spec, prefix):
        with working_dir('pio'):
            make(parallel = False)

    def install(self, spec, prefix):
        with working_dir('pio'):
            make('install')
