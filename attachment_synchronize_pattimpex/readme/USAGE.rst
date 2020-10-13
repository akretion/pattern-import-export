Imports
=======

Make sure you have a cron that calls run_import_scheduler()

Create a Task of import type, pick a file pattern, an export pattern (ir.exports)

In your storage, add files of the appropriate format (csv or excel) and wait for the 2 successive crons to run.

Exports
=======

Create a Task of export type. Choose a patterned export and a domain for the records you want to export.

Create a cron that runs on your specific export task service_trigger_export()

Create a cron that runs on your specific export task run_export()

Observe that your storage gets filled with files of the appropriate format (csv/excel) with the records specified in your export domain.
