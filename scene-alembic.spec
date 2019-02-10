#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scene-alembic
Version  : 1.7.10
Release  : 3
URL      : https://github.com/alembic/alembic/archive/1.7.10.tar.gz
Source0  : https://github.com/alembic/alembic/archive/1.7.10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: scene-alembic-bin = %{version}-%{release}
Requires: scene-alembic-lib = %{version}-%{release}
Requires: scene-alembic-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : hdf5-dev
BuildRequires : openexr-dev
BuildRequires : zlib-dev

%description
AlembicRiProcedural usage:
-filename /path/to/some/archive.abc
This is the only required argument. It has no default value.

%package bin
Summary: bin components for the scene-alembic package.
Group: Binaries
Requires: scene-alembic-license = %{version}-%{release}

%description bin
bin components for the scene-alembic package.


%package dev
Summary: dev components for the scene-alembic package.
Group: Development
Requires: scene-alembic-lib = %{version}-%{release}
Requires: scene-alembic-bin = %{version}-%{release}
Provides: scene-alembic-devel = %{version}-%{release}

%description dev
dev components for the scene-alembic package.


%package lib
Summary: lib components for the scene-alembic package.
Group: Libraries
Requires: scene-alembic-license = %{version}-%{release}

%description lib
lib components for the scene-alembic package.


%package license
Summary: license components for the scene-alembic package.
Group: Default

%description license
license components for the scene-alembic package.


%prep
%setup -q -n alembic-1.7.10

%build
## build_prepend content
sed -i -e 's/ConfigPackageLocation lib/ConfigPackageLocation %{_lib}/g' \
lib/Alembic/CMakeLists.txt
iconv -f iso8859-1 -t utf-8 ACKNOWLEDGEMENTS.txt > ACKNOWLEDGEMENTS.txt.conv && \
mv -f ACKNOWLEDGEMENTS.txt.conv ACKNOWLEDGEMENTS.txt
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545251328
mkdir -p clr-build
pushd clr-build
%cmake .. -DALEMBIC_LIB_INSTALL_DIR=%{_libdir} \
-DALEMBIC_SHARED_LIBS=ON \
-DUSE_BINARIES=ON \
-DUSE_HDF5=ON \
-DUSE_EXAMPLES=ON \
-DUSE_PYALEMBIC=OFF \
-DUSE_STATIC_BOOST=OFF \
-DUSE_STATIC_HDF5=OFF \
-DUSE_TESTS=ON
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1545251328
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scene-alembic
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/scene-alembic/LICENSE.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/abcconvert
/usr/bin/abcdiff
/usr/bin/abcecho
/usr/bin/abcechobounds
/usr/bin/abcls
/usr/bin/abcstitcher
/usr/bin/abctree

%files dev
%defattr(-,root,root,-)
/usr/include/Alembic/Abc/All.h
/usr/include/Alembic/Abc/ArchiveInfo.h
/usr/include/Alembic/Abc/Argument.h
/usr/include/Alembic/Abc/Base.h
/usr/include/Alembic/Abc/ErrorHandler.h
/usr/include/Alembic/Abc/Foundation.h
/usr/include/Alembic/Abc/IArchive.h
/usr/include/Alembic/Abc/IArrayProperty.h
/usr/include/Alembic/Abc/IBaseProperty.h
/usr/include/Alembic/Abc/ICompoundProperty.h
/usr/include/Alembic/Abc/IObject.h
/usr/include/Alembic/Abc/ISampleSelector.h
/usr/include/Alembic/Abc/IScalarProperty.h
/usr/include/Alembic/Abc/ISchema.h
/usr/include/Alembic/Abc/ISchemaObject.h
/usr/include/Alembic/Abc/ITypedArrayProperty.h
/usr/include/Alembic/Abc/ITypedScalarProperty.h
/usr/include/Alembic/Abc/OArchive.h
/usr/include/Alembic/Abc/OArrayProperty.h
/usr/include/Alembic/Abc/OBaseProperty.h
/usr/include/Alembic/Abc/OCompoundProperty.h
/usr/include/Alembic/Abc/OObject.h
/usr/include/Alembic/Abc/OScalarProperty.h
/usr/include/Alembic/Abc/OSchema.h
/usr/include/Alembic/Abc/OSchemaObject.h
/usr/include/Alembic/Abc/OTypedArrayProperty.h
/usr/include/Alembic/Abc/OTypedScalarProperty.h
/usr/include/Alembic/Abc/Reference.h
/usr/include/Alembic/Abc/SourceName.h
/usr/include/Alembic/Abc/TypedArraySample.h
/usr/include/Alembic/Abc/TypedPropertyTraits.h
/usr/include/Alembic/AbcCollection/All.h
/usr/include/Alembic/AbcCollection/ICollections.h
/usr/include/Alembic/AbcCollection/OCollections.h
/usr/include/Alembic/AbcCollection/SchemaInfoDeclarations.h
/usr/include/Alembic/AbcCoreAbstract/All.h
/usr/include/Alembic/AbcCoreAbstract/ArchiveReader.h
/usr/include/Alembic/AbcCoreAbstract/ArchiveWriter.h
/usr/include/Alembic/AbcCoreAbstract/ArrayPropertyReader.h
/usr/include/Alembic/AbcCoreAbstract/ArrayPropertyWriter.h
/usr/include/Alembic/AbcCoreAbstract/ArraySample.h
/usr/include/Alembic/AbcCoreAbstract/ArraySampleKey.h
/usr/include/Alembic/AbcCoreAbstract/BasePropertyReader.h
/usr/include/Alembic/AbcCoreAbstract/BasePropertyWriter.h
/usr/include/Alembic/AbcCoreAbstract/CompoundPropertyReader.h
/usr/include/Alembic/AbcCoreAbstract/CompoundPropertyWriter.h
/usr/include/Alembic/AbcCoreAbstract/DataType.h
/usr/include/Alembic/AbcCoreAbstract/ForwardDeclarations.h
/usr/include/Alembic/AbcCoreAbstract/Foundation.h
/usr/include/Alembic/AbcCoreAbstract/MetaData.h
/usr/include/Alembic/AbcCoreAbstract/ObjectHeader.h
/usr/include/Alembic/AbcCoreAbstract/ObjectReader.h
/usr/include/Alembic/AbcCoreAbstract/ObjectWriter.h
/usr/include/Alembic/AbcCoreAbstract/PropertyHeader.h
/usr/include/Alembic/AbcCoreAbstract/ReadArraySampleCache.h
/usr/include/Alembic/AbcCoreAbstract/ScalarPropertyReader.h
/usr/include/Alembic/AbcCoreAbstract/ScalarPropertyWriter.h
/usr/include/Alembic/AbcCoreAbstract/ScalarSample.h
/usr/include/Alembic/AbcCoreAbstract/TimeSampling.h
/usr/include/Alembic/AbcCoreAbstract/TimeSamplingType.h
/usr/include/Alembic/AbcCoreFactory/All.h
/usr/include/Alembic/AbcCoreFactory/IFactory.h
/usr/include/Alembic/AbcCoreHDF5/All.h
/usr/include/Alembic/AbcCoreHDF5/ReadWrite.h
/usr/include/Alembic/AbcCoreLayer/Foundation.h
/usr/include/Alembic/AbcCoreLayer/Read.h
/usr/include/Alembic/AbcCoreLayer/Util.h
/usr/include/Alembic/AbcCoreOgawa/All.h
/usr/include/Alembic/AbcCoreOgawa/ReadWrite.h
/usr/include/Alembic/AbcGeom/All.h
/usr/include/Alembic/AbcGeom/ArchiveBounds.h
/usr/include/Alembic/AbcGeom/Basis.h
/usr/include/Alembic/AbcGeom/CameraSample.h
/usr/include/Alembic/AbcGeom/CurveType.h
/usr/include/Alembic/AbcGeom/FaceSetExclusivity.h
/usr/include/Alembic/AbcGeom/FilmBackXformOp.h
/usr/include/Alembic/AbcGeom/Foundation.h
/usr/include/Alembic/AbcGeom/GeometryScope.h
/usr/include/Alembic/AbcGeom/ICamera.h
/usr/include/Alembic/AbcGeom/ICurves.h
/usr/include/Alembic/AbcGeom/IFaceSet.h
/usr/include/Alembic/AbcGeom/IGeomBase.h
/usr/include/Alembic/AbcGeom/IGeomParam.h
/usr/include/Alembic/AbcGeom/ILight.h
/usr/include/Alembic/AbcGeom/INuPatch.h
/usr/include/Alembic/AbcGeom/IPoints.h
/usr/include/Alembic/AbcGeom/IPolyMesh.h
/usr/include/Alembic/AbcGeom/ISubD.h
/usr/include/Alembic/AbcGeom/IXform.h
/usr/include/Alembic/AbcGeom/OCamera.h
/usr/include/Alembic/AbcGeom/OCurves.h
/usr/include/Alembic/AbcGeom/OFaceSet.h
/usr/include/Alembic/AbcGeom/OGeomBase.h
/usr/include/Alembic/AbcGeom/OGeomParam.h
/usr/include/Alembic/AbcGeom/OLight.h
/usr/include/Alembic/AbcGeom/ONuPatch.h
/usr/include/Alembic/AbcGeom/OPoints.h
/usr/include/Alembic/AbcGeom/OPolyMesh.h
/usr/include/Alembic/AbcGeom/OSubD.h
/usr/include/Alembic/AbcGeom/OXform.h
/usr/include/Alembic/AbcGeom/SchemaInfoDeclarations.h
/usr/include/Alembic/AbcGeom/Visibility.h
/usr/include/Alembic/AbcGeom/XformOp.h
/usr/include/Alembic/AbcGeom/XformSample.h
/usr/include/Alembic/AbcMaterial/All.h
/usr/include/Alembic/AbcMaterial/IMaterial.h
/usr/include/Alembic/AbcMaterial/MaterialAssignment.h
/usr/include/Alembic/AbcMaterial/MaterialFlatten.h
/usr/include/Alembic/AbcMaterial/OMaterial.h
/usr/include/Alembic/AbcMaterial/SchemaInfoDeclarations.h
/usr/include/Alembic/Util/All.h
/usr/include/Alembic/Util/Config.h
/usr/include/Alembic/Util/Digest.h
/usr/include/Alembic/Util/Dimensions.h
/usr/include/Alembic/Util/Exception.h
/usr/include/Alembic/Util/Export.h
/usr/include/Alembic/Util/Foundation.h
/usr/include/Alembic/Util/Murmur3.h
/usr/include/Alembic/Util/Naming.h
/usr/include/Alembic/Util/OperatorBool.h
/usr/include/Alembic/Util/PlainOldDataType.h
/usr/include/Alembic/Util/SpookyV2.h
/usr/include/Alembic/Util/TokenMap.h
/usr/lib64/cmake/Alembic/AlembicConfig.cmake
/usr/lib64/cmake/Alembic/AlembicConfigVersion.cmake
/usr/lib64/cmake/Alembic/AlembicTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Alembic/AlembicTargets.cmake
/usr/lib64/libAlembic.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libAlembic.so.1.7
/usr/lib64/libAlembic.so.1.7.10

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scene-alembic/LICENSE.txt
