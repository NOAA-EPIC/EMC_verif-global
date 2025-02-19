help([[
Load environment to run EMC_verif-global on Gaea-C5 using Intel
]])

prepend_path("MODULEPATH", "/ncrc/proj/epic/spack-stack/spack-stack-1.6.0/envs/gsi-addon-dev/install/modulefiles/Core")

stack_intel_ver=os.getenv("stack_intel_ver") or "2023.2.0"
load(pathJoin("stack-intel", stack_intel_ver))

Core_ver=os.getenv("Core_ver") or "24.11"
load(pathJoin("Core", Core_ver))

prod_util_ver=os.getenv("prod_util_ver") or "2.1.1"
load(pathJoin("prod_util", prod_util_ver))

grib_util_ver=os.getenv("grib_util_ver") or "1.3.0"
load(pathJoin("grib-util", grib_util_ver))

intel_oneapi_ver=os.getenv("stack_cray_mpich_ver") or "8.1.28"
load(pathJoin("stack-cray-mpich", stack_cray_mpich_ver))

netcdf_c_ver=os.getenv("netcdf_c_ver") or "4.9.2"
load(pathJoin("netcdf-c", netcdf_c_ver))

nco_ver=os.getenv("nco_ver") or "5.1.9"
load(pathJoin("nco", nco_ver))

grads_ver=os.getenv("grads_ver") or "2.2.3"
load(pathJoin("grads", grads_ver))

imagemagick_ver=os.getenv("imagemagick_ver") or "7.1.1-29"
load(pathJoin("imagemagick", imagemagick_ver))

met_ver=os.getenv("met_ver") or "9.1.3"
load(pathJoin("met", met_ver))

metplus_ver=os.getenv("metplus_ver") or "3.1.1"
load(pathJoin("metplus", metplus_ver))
