# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ndarray(CMakePackage):
    """Ndarray is a basic component for FTK"""

    # Add a proper url for your package's homepage here.
    homepage = "https://github.com/hguo/ndarray"
    git = "https://github.com/hguo/ndarray.git"

    # Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("hguo")

    license("MIT")

    version("main", branch="main")

    # variants
    variant("adios2", default=False, description="Use ADIOS2")
    variant("cuda", default=False, description="Use CUDA")
    variant("hdf5", default=False, description="Use HDF5")
    variant("mpi", default=False, description="Use MPI")
    variant("netcdf", default=False, description="Use NetCDF")
    variant("vtk", default=False, description="Use VTK")

    # optional dependencies
    depends_on("adios2", when="+adios2")
    depends_on("cuda", when="+cuda")
    depends_on("hdf5", when="+hdf5")
    depends_on("mpi", when="+mpi")
    depends_on("netcdf-c", when="+netcdf")
    depends_on("vtk", when="+vtk")
    depends_on("yaml-cpp")

    def add_cmake_option(self, args, dependency, option):
        if dependency in self.spec:
            args.append("-D" + option + "=ON")
        else:
            args.append("-D" + option + "=OFF")

    def cmake_args(self):
        args = []

        self.add_cmake_option(args, "+adios2", "NDARRAY_USE_ADIOS2")
        self.add_cmake_option(args, "+cuda", "NDARRAY_USE_CUDA")
        self.add_cmake_option(args, "+hdf5", "NDARRAY_USE_HDF5")
        self.add_cmake_option(args, "+mpi", "NDARRAY_USE_MPI")
        self.add_cmake_option(args, "+netcdf", "NDARRAY_USE_NETCDF")
        self.add_cmake_option(args, "+vtk", "NDARRAY_USE_VTK")

        return args
