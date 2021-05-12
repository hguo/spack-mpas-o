# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class MpasOcean(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/MPAS-Dev/MPAS-Model/archive/refs/tags/v6.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('6.0', 'b5c0000be0a6bececf4426cdf946cba0727b69985478ded0011ec31282c75105')
    version('mraj', git='https://github.com/mukundraj/MPAS-Model.git', branch='v6.0_decaf-hooks')
    version('pwolfram', commit='243471f462f0500debee2017fa9ec54adb07ea65', git='https://github.com/pwolfram/MPAS-Model')

    patch('patch')
    patch('patch1', when='@mraj')

    depends_on('mpich@3.2.1 device=ch3')
    depends_on('pio@1_7_2', type='link')
    depends_on('hdf5@1.10.2')
    depends_on('netcdf-c@4.6.1 +mpi', type='link')
    depends_on('netcdf-fortran@4.4.4', type='link')
    depends_on('parallel-netcdf@1.7.0 -shared', type='link')
    # depends_on('python@:2.9', type='build')
    depends_on('python@3:', type='build')

    depends_on('decaf@mraj', type=('link', 'run'), when='@mraj')

    phases = ['build', 'install']

    def target(self):
        spec = self.spec
        target = [
                'gfortran',
                'NETCDF={0}'.format(spec['netcdf-c'].prefix), 
                'NETCDFF={0}'.format(spec['netcdf-fortran'].prefix),
                'PNETCDF={0}'.format(spec['parallel-netcdf'].prefix),
                # 'DECAF={0}'.format(spec['decaf'].prefix)
                'PIO={0}'.format(spec['pio'].prefix),
                # 'FFLAGS={0}'.format('-mcmodel=large'),
                'CORE=ocean'
                ]

        if (self.spec.satisfies('@mraj')):
            target.append('DECAF_FOLDER={0}'.format(spec['decaf'].prefix))

        return target

    def build(self, spec, prefix):
        make(*self.target(), parallel=False)
        mkdir('bin')
        copy('ocean_model', 'bin')

    def install(self, spec, prefix):
        install_tree('bin', prefix.bin)
