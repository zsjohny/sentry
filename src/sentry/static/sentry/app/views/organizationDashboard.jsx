import React from 'react';
import {Link} from 'react-router';
import {Sparklines, SparklinesLine} from 'react-sparklines';

import ActivityFeed from '../components/activity/feed';
import GroupStore from '../stores/groupStore';
import IssueList from '../components/issueList';
import OrganizationHomeContainer from '../components/organizations/homeContainer';
import OrganizationState from '../mixins/organizationState';
import {t} from '../locale';
import {sortArray} from '../utils';

const AssignedIssues = React.createClass({
  propTypes: {
    statsPeriod: React.PropTypes.string,
    pageSize: React.PropTypes.number
  },

  getEndpoint() {
    return `/organizations/${this.props.params.orgId}/members/me/issues/assigned/?`;
  },

  getViewMoreLink() {
    return `/organizations/${this.props.params.orgId}/issues/assigned/`;
  },

  render() {
    return (
      <div>
        <div className="pull-right">
          <Link className="btn btn-sm btn-default" to={this.getViewMoreLink()}>{t('View more')}</Link>
        </div>
        <h3>Assigned</h3>
        <IssueList endpoint={this.getEndpoint()} query={{
          statsPeriod: this.props.statsPeriod,
          per_page: this.props.pageSize,
          status: 'unresolved',
        }} pagination={false} {...this.props} />
      </div>
    );
  },
});

const NewIssues = React.createClass({
  propTypes: {
    statsPeriod: React.PropTypes.string,
    pageSize: React.PropTypes.number
  },

  getEndpoint() {
    return `/organizations/${this.props.params.orgId}/issues/new/`;
  },

  render() {
    return (
      <div>
        <h3>New</h3>
        <IssueList endpoint={this.getEndpoint()} query={{
          statsPeriod: this.props.statsPeriod,
          per_page: this.props.pageSize,
          status: 'unresolved',
        }} pagination={false} {...this.props} />
      </div>
    );
  },
});

function ProjectSparkline(props) {
  let values = props.data.map(tuple => tuple[1]);

  let max = Math.max.apply(Math.max, values);

  const WIDTH = 120;

  if (max > 0) {
    return (
      <Sparklines data={values}>
        <SparklinesLine {...props} style={{stroke: '#24A6F7', fill: 'none', strokeWidth: 3}}/>
      </Sparklines>
    );
  } else {
    // react-sparklines does not like flat lines, so lets make them ourselves
    // https://github.com/borisyankov/react-sparklines/issues/39
    //
    // NOTE: this little hack means that project stats w/ the same event count for each entry
    //       will not render! I'm just kind of counting on that being very unlikely; when the PR
    //       for react-sparklines is accepted, we'll remove this.
    let coords = values.map((_, idx) => {
      return (WIDTH / values.length) * idx + ' 28';
    }).join(' ');

    return (
      <svg width="120" height="30">
        <g>
          <polyline points={coords} style={{stroke: '#24A6F7', strokeWidth: 3, strokeLinejoin:'round', strokeLinecap:'round', fill:'none'}}/>
        </g>
      </svg>
    );
  }
}
ProjectSparkline.propTypes = {
  data: React.PropTypes.array.isRequired
};

const ProjectList = React.createClass({
  propTypes: {
    maxProjects: React.PropTypes.number
  },

  mixins: [OrganizationState],

  getDefaultProps() {
    return {
      maxProjects: 10,
    };
  },

  render() {
    let org = this.getOrganization();
    let maxProjects = this.props.maxProjects;
    let projectList = [];
    org.teams.forEach((team) => {
      team.projects.forEach((project) => {
        projectList.push({...project, teamName: team.name});
      });
    });

    projectList = sortArray(projectList, (item) => {
      return [!item.isBookmarked, item.teamName, item.name];
    });

    return (
      <div className="organization-dashboard-projects">
        {projectList.length > maxProjects &&
          <div className="pull-right">
            <Link className="btn btn-sm btn-default"
                  to={`/{$org.slug}/`}>View All</Link>
          </div>
        }
        <h6 className="nav-header">Projects</h6>
        <ul className="nav nav-stacked">
          {projectList.slice(0, maxProjects).map((project) => {
            return (
              <li key={project.id}>
                <div className="pull-right">
                  {project.stats &&
                    <ProjectSparkline data={project.stats}/>
                  }
                </div>
                <Link to={`/${org.slug}/${project.slug}/`}>
                  <h4>
                    {project.isBookmarked &&  <span className="bookmark icon-bookmark"></span>}
                    {project.name}
                  </h4>
                  <h5>{project.teamName}</h5>
                </Link>
              </li>
            );
          })}
        </ul>
      </div>
    );
  },
});

const Activity = React.createClass({

  getEndpoint() {
    return `/organizations/${this.props.params.orgId}/activity/`;
  },

  render() {
    return (
      <div>
        <h6 className="nav-header">Activity</h6>
        <ActivityFeed endpoint={this.getEndpoint()} query={{
          per_page: 10,
        }} pagination={false} {...this.props} />
      </div>
    );
  },
});

const OrganizationDashboard = React.createClass({
  getDefaultProps() {
    return {
      statsPeriod: '24h',
      pageSize: 5,
    };
  },

  componentWillUnmount() {
    GroupStore.reset();
  },

  render() {
    return (
      <OrganizationHomeContainer>
        <div className="early-adopter-banner"><strong>Psst!</strong> This feature is still a work-in-progress. Thanks for being an early adopter!</div>
        <div className="row">
          <div className="col-md-8">
            <AssignedIssues {...this.props} />
            <NewIssues {...this.props} />
          </div>
          <div className="col-md-4">
            <ProjectList {...this.props} />
            <Activity {...this.props} />
          </div>
        </div>
      </OrganizationHomeContainer>
    );
  },
});

export default OrganizationDashboard;
