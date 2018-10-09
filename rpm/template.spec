Name:           ros-melodic-marti-status-msgs
Version:        0.7.0
Release:        0%{?dist}
Summary:        ROS marti_status_msgs package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_messages
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-std-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-std-msgs

%description
marti_status_msgs

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Oct 09 2018 Marc Alban <malban@swri.org> - 0.7.0-0
- Autogenerated by Bloom

* Thu May 24 2018 Marc Alban <malban@swri.org> - 0.6.0-0
- Autogenerated by Bloom

* Fri May 11 2018 Marc Alban <malban@swri.org> - 0.5.0-0
- Autogenerated by Bloom

