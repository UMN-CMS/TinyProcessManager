: ${BUILDDIR:=BUILD}
: ${TPM_VERSION:=0.0.1}
: ${TPM_RELEASE:=NORELEASE}

rm -fr "$BUILDDIR"
mkdir -p "${BUILDDIR}"/{RPMS,SOURCES,SPECS,SRPMS,BUILD}
tar czf $BUILDDIR/SOURCES/tiny_process_manager-${TPM_VERSION}-${TPM_RELEASE}.tar.gz tiny_process_manager tiny_process_manager.service
cp tinypm.spec $BUILDDIR/SPECS

rpmbuild --define "_topdir $(realpath BUILD)" -ba BUILD/SPECS/tinypm.spec
