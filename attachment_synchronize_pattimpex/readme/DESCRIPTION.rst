This module uses the pattern_import_export and attachment_synchronize modules to automate imports and exports.

The flows work as follows :

Imports
=======

attachment_synchronize:

* A cron calls run_import_scheduler() on all synchronization tasks

* attachment.queue of the appropriate type is generated, this means the file is imported into an attachment

* Another cron calls run_export_scheduler() **(which is a misnomer)** -> patterned.import.export is generated

pattern_import_export:

* patterned.import.export imports the file

Exports
=======

pattern_import_export:

* A cron triggers service_trigger_exports() for a specific task

* pattern.import.export is created, exporting records using domain specified in task -> xlsx

attachment_synchronize:

* A cron triggers run_export_scheduler on the same task (i.e the export of the xlsx to the storage space)
