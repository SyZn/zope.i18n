##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id: negotiator.py,v 1.2 2002/12/25 14:13:39 jim Exp $
"""

from zope.interfaces.i18n import INegotiator
from zope.interfaces.i18n import IUserPreferredLanguages
from zope.interfaces.i18n import ILanguageAvailability
from zope.component import getAdapter

class Negotiator:

    __implements__ = INegotiator

    def getLanguage(self, langs, env):
        envadaptor = getAdapter(env, IUserPreferredLanguages)
        userlangs = envadaptor.getPreferredLanguages()
        # Prioritize on the user preferred languages.  Return the first user
        # preferred language that the object has available.
        for lang in userlangs:
            if lang in langs:
                return lang
        return None


negotiator = Negotiator()